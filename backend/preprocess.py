import os
import pandas as pd

def preprocess_data():
    # Path to the dataset
    lines_path = os.path.join('data', 'cornell movie-dialogs corpus', 'movie_lines.txt')
    conversations_path = os.path.join('data', 'cornell movie-dialogs corpus', 'movie_conversations.txt')

    # Read lines
    lines = open(lines_path, encoding='utf-8', errors='ignore').read().split('\n')
    id2line = {line.split(' +++$+++ ')[0]: line.split(' +++$+++ ')[-1] for line in lines}

    # Read conversations
    conversations = open(conversations_path, encoding='utf-8', errors='ignore').read().split('\n')
    conversation_ids = [conv.split(' +++$+++ ')[-1][1:-1].replace("'", "").split(", ") for conv in conversations]

    # Extract question-answer pairs
    questions, answers = [], []
    for conversation in conversation_ids:
        for i in range(len(conversation) - 1):
            questions.append(id2line.get(conversation[i], ""))
            answers.append(id2line.get(conversation[i + 1], ""))

    # Save to CSV for later use
    df = pd.DataFrame({'question': questions, 'answer': answers})
    df = df.dropna()
    df.to_csv('data/preprocessed_data.csv', index=False)

    print("Preprocessing completed. Data saved to 'data/preprocessed_data.csv'.")

if __name__ == "__main__":
    preprocess_data()
