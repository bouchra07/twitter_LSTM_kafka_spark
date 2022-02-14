import os, string
import numpy as np

import pickle
import keras.models
from keras.models import Sequential
from keras.layers import Embedding
from keras.layers.recurrent import LSTM
from keras.layers import Input, Dense, Embedding, SpatialDropout1D, add, concatenate
from keras.callbacks import ModelCheckpoint, EarlyStopping
from .CleanText import CleanText
from keras.preprocessing.sequence import pad_sequences

import re
from nltk.corpus import stopwords

class MulticlassComplainInference:

    def __init__(self):
        self.load_models()
        self.MAX_NB_WORDS = 50000
        self.MAX_SEQUENCE_LENGTH = 250
        self.EMBEDDING_DIM = 100
        self.clean_text = CleanText()

    def get_model(self, input_len):
        model = Sequential()
        model.add(Embedding(self.MAX_NB_WORDS, self.EMBEDDING_DIM, input_length=input_len))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(8, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def load_models(self):
        with open('../model_multiclass/tokenizerMulticlassComplaintClassification.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

        self.model = self.get_model(self.MAX_SEQUENCE_LENGTH)
        self.model.load_weights("../model_multiclass/multiclassComplaintClassifier.h5")

    def predict_complaint(self, text):
        new_tweet = self.clean_text.clean_text(text)
        seq = self.tokenizer.texts_to_sequences([new_tweet])
        padded = pad_sequences(seq, maxlen=self.MAX_SEQUENCE_LENGTH)
        pred = self.model.predict(padded)
        labels = ['Reschedule and Refund', 'Baggage Issue', 'Phone and Online Booking', 'Extra Charges',
                  'Delay and Customer Service', 'Seating Preferences', 'Reservation Issue', 'Customer Experience']
        print(pred, labels[np.argmax(pred)])
        return labels[np.argmax(pred)]
