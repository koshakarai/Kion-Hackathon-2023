"""
This file contains code for sampling caption using the model built (default: sample_model.h5)
It will first convert all the images from the sample_images folder into a set of VGG16 features, 
and then pass the features to the trained deep-learning model and tokenizer,
and return the captions.
"""

import os
import keras
from keras.preprocessing.text import tokenizer_from_json
import keras.utils as image
import numpy as np
from .__init__ import model, tokenizer, vocab_size, max_length

from .build_model.build import feature_extractions, feature_extraction_file, sample_caption
import json
from pickle import load, dump
    
def GICD(dirictory):
    #Load tokenizer
    print('asd')
    with open('./tokenizer.json', 'r') as f:
        tokenizer_json = json.load(f)
    tokenizer = tokenizer_from_json(tokenizer_json)
        
    model = keras.models.load_model("./sample_model.h5") #Load model
    vocab_size = tokenizer.num_words #The number of vocabulary
    max_length = 37 #Maximum length of caption sequence

    #sampling
    features = feature_extractions(dirictory)

    for i, filename in enumerate(features.keys()):
        caption = sample_caption(model, tokenizer, max_length, vocab_size, features[filename])
        print(caption)

def GIC(file):
    #Load tokenizer


    #sampling
    feature = feature_extraction_file(file)

    caption = sample_caption(model, tokenizer, max_length, vocab_size, feature)
    return caption
