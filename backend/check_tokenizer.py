import pickle

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

# Print the tokenizer's word index
print("Word Index:", tokenizer.word_index)

# Check if a specific word exists in the vocabulary
word = "hello"
if word in tokenizer.word_index:
    print(f"The word '{word}' is in the vocabulary with index {tokenizer.word_index[word]}")
else:
    print(f"The word '{word}' is not in the vocabulary.")
