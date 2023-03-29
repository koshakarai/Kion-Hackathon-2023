import os
import keras
import json
from keras.preprocessing.text import tokenizer_from_json

print(os.getcwd())
with open(f'{os.getcwd()}/ICG/tokenizer.json', 'r') as f:
    tokenizer_json = json.load(f)
tokenizer = tokenizer_from_json(tokenizer_json)
        
model = keras.models.load_model(f'{os.getcwd()}/ICG/sample_model.h5') #Load model
vocab_size = tokenizer.num_words #The number of vocabulary
max_length = 37 #Maximum length of caption sequence