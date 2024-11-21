from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
import pickle

app = Flask(__name__)

# Load the trained model
model = load_model('chatbot_model.h5')

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

# Define a function to decode the model's predictions
def decode_sequence(input_seq):
    # Build encoder model
    encoder_model = tf.keras.Model(inputs=model.input[0], outputs=model.layers[4].output[1:])
    
    # Build decoder model
    decoder_inputs = model.input[1]  # Decoder input
    decoder_state_input_h = tf.keras.Input(shape=(256,), name="decoder_state_input_h")
    decoder_state_input_c = tf.keras.Input(shape=(256,), name="decoder_state_input_c")
    decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

    decoder_lstm = model.layers[5]  # The LSTM layer from the original decoder
    decoder_embedding = model.layers[3]  # The embedding layer
    decoder_dense = model.layers[-1]  # The Dense layer

    # Get the outputs of the decoder
    decoder_outputs, state_h, state_c = decoder_lstm(
        decoder_embedding(decoder_inputs),
        initial_state=decoder_states_inputs,
    )
    decoder_states = [state_h, state_c]
    decoder_outputs = decoder_dense(decoder_outputs)

    decoder_model = tf.keras.Model(
        [decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states
    )

    # Encode the input as states
    state_h, state_c = encoder_model.predict(input_seq)
    states_value = [state_h, state_c]

    # Start token for decoder
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = tokenizer.word_index.get('<start>', 1)  # Default to 1 if '<start>' is missing

    # Generate the response sentence
    decoded_sentence = ""
    stop_condition = False

    while not stop_condition:
        decoder_outputs, h, c = decoder_model.predict([target_seq] + states_value)

        # Sample a token
        sampled_token_index = np.argmax(decoder_outputs[0, -1, :])
        sampled_word = tokenizer.index_word.get(sampled_token_index, "<unk>")

        if sampled_word == "<end>" or len(decoded_sentence) > 50:
            stop_condition = True
        else:
            decoded_sentence += " " + sampled_word

        # Update target sequence and states
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index
        states_value = [h, c]

    return decoded_sentence.strip()


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_message = data.get('message', '')

    # Preprocess the input message
    input_seq = tokenizer.texts_to_sequences([input_message])
    input_padded = tf.keras.preprocessing.sequence.pad_sequences(input_seq, maxlen=20, padding='post')

    # Get the response from the model
    response = decode_sequence(input_padded)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)

