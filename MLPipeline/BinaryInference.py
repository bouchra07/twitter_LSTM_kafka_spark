from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
import pickle
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers import Input, Dense, Embedding, SpatialDropout1D, add, concatenate
import numpy as np
from .CleanText import CleanText

class BinaryInference:
      def __init__(self):
          self.load_models()
          self.clean_text = CleanText()

      def get_model(self):
          max_fatures = 2000
          embed_dim = 128
          lstm_out = 196
          input_len = 21
          model = Sequential()
          model.add(Embedding(max_fatures, embed_dim,input_length = input_len))
          model.add(SpatialDropout1D(0.4))
          model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
          model.add(Dense(2,activation='softmax'))
          model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

          return model

      def load_models(self):
          with open('../models/model_binaryclass/tokenizerBinaryClassification.pickle', 'rb') as handle:
              self.tokenizer = pickle.load(handle)

          self.model = self.get_model()
          self.model.load_weights("../models/model_binaryclass/binaryClassificationModel.h5")


      def predict_complaint(self, text):

          text = self.clean_text.clean_text(text)
          twt = self.tokenizer.texts_to_sequences([text])
          twt = pad_sequences(twt, maxlen=21, dtype='èint32', value=0)
          complain = self.model.predict(twt,batch_size=1,verbose = 0)[0]
          if(np.argmax(complain) == 0):
              print("negative")
              return True
          elif (np.argmax(complain) == 1):
              print("positive")
              return False