import streamlit as st
import random
import pandas as pd
import numpy as np
import csv

import random
from collections import defaultdict

with st.columns(3)[1]:
    st.title('Generate Headlines for articles')
st.divider()
file_id = '1XKsJ8broAJYpwK7YUqZTftpaUtLaBU9H'
link = f'https://drive.google.com/uc?id={file_id}'
#df = pd.read_csv(link,usecols=['headline'])
df = pd.read_csv(link)
data=df['headline']

sentences=data

# Preprocess the dataset and extract words
words = [word.lower() for sentence in sentences for word in sentence.split()]

load=st.button('Generate Headline')
if load:
    
# Build a transition matrix
    transition_matrix = defaultdict(list)
    for i in range(len(words) - 1):
        transition_matrix[words[i]].append(words[i + 1])
 
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
        # generated_sentence.append(generated_sentence)
        
        st.subheader(generated_sentence)
    
