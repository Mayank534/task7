

from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS module
import random
from collections import defaultdict

from flask import Flask
app=Flask(__name__)
generated_sentences = []

@app.route("/hello", methods = ['GET'])
def generate_sentence():
    import pandas as pd
    import numpy as np
    import csv

    import random
    from collections import defaultdict

    file_id = '1XKsJ8broAJYpwK7YUqZTftpaUtLaBU9H'
    link = f'https://drive.google.com/uc?id={file_id}'
#df = pd.read_csv(link,usecols=['headline'])
    df = pd.read_csv(link)
    data=df['headline']

    sentences=data

# Preprocess the dataset and extract words
    words = [word.lower() for sentence in sentences for word in sentence.split()]

# Build a transition matrix
    transition_matrix = defaultdict(list)
    for i in range(len(words) - 1):
        transition_matrix[words[i]].append(words[i + 1])


    file_id = '1XKsJ8broAJYpwK7YUqZTftpaUtLaBU9H'
    link = f'https://drive.google.com/uc?id={file_id}'
#df = pd.read_csv(link,usecols=['headline'])
    df = pd.read_csv(link)
    data=df['headline']

    num_sentences = 1  # Number of sentences to generate
    max_sentence_length = random.randint(5,12)  # Maximum length of each sentence

    

    for _ in range(num_sentences):
        sentence = []
        current_word = random.choice(words)
        sentence.append(current_word)

        while len(sentence) < max_sentence_length:
            next_word_options = transition_matrix[current_word]
            if not next_word_options:
                break
            next_word = max(set(next_word_options), key=next_word_options.count)
            sentence.append(next_word)
            current_word = next_word

        generated_sentence = " ".join(sentence)
        generated_sentences.append(generated_sentence)
        
        
    return jsonify(generated_sentences)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
