import numpy as np
import pandas as pd
import os
import pickle
import spacy
import spacy.cli

import spacy
nlp = spacy.load('en_core_web_lg')



with open('model.pkl', 'rb') as f:
   model = pickle.load(f)

with open('scaler.pkl', 'rb') as f1:
   scaler = pickle.load(f1)

df=pd.read_csv('Symptom2Disease.csv', index_col=0)
lookup=dict(zip(df.label.unique(),pd.Series([i for i in range(24)])))


nlp=spacy.load('en_core_web_lg')


def preprocess(text):
    list=[]
    for token in nlp(text):
        if token.is_space or token.is_punct:
            continue
        list.append(token.lemma_)
    return ' '.join(list)


def predict(data):
    tp=preprocess(data)
    tp = nlp(tp).vector
    tp = tp.reshape(1, -1)
    tp = scaler.transform(tp)
    pred = model.predict(tp)
    value=[i for i in lookup if lookup[i]==pred[0]]
    return value[0]
