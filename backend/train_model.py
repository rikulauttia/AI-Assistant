import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense
import pandas as pd
import numpy as np
import os

# Load preprocessed data
data_path = os.path.join('data', 'preprocessed_data.csv')
data = pd.read_csv(data_path)

# Clean non-string values
data['question'] = data['question'].fillna("").astype(str)
data['answer'] = data['answer'].fillna("").astype(str)

# Optional: Remove empty questions and answers
data = data[(data['question'] != "") & (data['answer'] != "")]

# Debug: Check for data types
print(data['question'].apply(type).value_counts())
print(data['answer'].apply(type).value_counts())

# Prepare input and output sequences
questions = data['question'].values[:10000]  # Limit to 10,000 pairs for simplicity
answers = data['answer'].values[:10000]

# Tokenization
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(questions + answers)
vocab_size = len(tokenizer.word_index) + 1

# Sequence encoding
question_sequences = tokenizer.texts_to_sequences(questions)
answer_sequences = tokenizer.texts_to_sequences(answers)

# Padding
max_len = 20
question_padded = tf.keras.preprocessing.sequence.pad_sequences(question_sequences, maxlen=max_len, padding='post')
answer_padded = tf.keras.preprocessing.sequence.pad_sequences(answer_sequences, maxlen=max_len, padding='post')

# Fix decoder input and target sequences to match max_len
decoder_inputs = tf.keras.preprocessing.sequence.pad_sequences(answer_padded[:, :-1], maxlen=max_len, padding='post')
decoder_targets = tf.keras.preprocessing.sequence.pad_sequences(answer_padded[:, 1:], maxlen=max_len, padding='post')

# Debug shapes
print("Question padded shape:", question_padded.shape)
print("Decoder inputs shape:", decoder_inputs.shape)
print("Decoder targets shape:", decoder_targets.shape)

# Define the model
embedding_dim = 128  # Choose the size of embeddings

# Define the encoder
encoder_inputs = Input(shape=(max_len,))
encoder_embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)(encoder_inputs)
encoder = LSTM(256, return_state=True)
encoder_outputs, state_h, state_c = encoder(encoder_embedding)
encoder_states = [state_h, state_c]

# Define the decoder
decoder_inputs_layer = Input(shape=(max_len,))
decoder_embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)(decoder_inputs_layer)
decoder_lstm = LSTM(256, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
decoder_dense = Dense(vocab_size, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Compile the model
model = Model([encoder_inputs, decoder_inputs_layer], decoder_outputs)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(
    [question_padded, decoder_inputs],
    decoder_targets,
    epochs=10,
    batch_size=64
)

# Save the model
model.save('chatbot_model.h5')
print("Model trained and saved as 'chatbot_model.h5'.")
