import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    T = len(series) - window_size
    for i in range(0, T):
        X.append(series[i:i + window_size])
        y.append(series[i + window_size])

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y), 1)

    return X, y


# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    rnn_model = Sequential()
    rnn_model.add(LSTM(5, input_shape=(window_size, 1)))
    rnn_model.add(Dense(1))

    return rnn_model


import string


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    # Get all the lowercase ascii
    ascii_low = string.ascii_lowercase

    # add lowercase ascii to allowed characters
    allowed_characters = punctuation
    for letter in ascii_low:
        allowed_characters.append(letter)

    for character in text:
        if character not in allowed_characters:
            text = text.replace(character, ' ')

    return text


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    T = len(text) - window_size

    for i in range(0, T, step_size):
        inputs.append(text[i:i + window_size])
        outputs.append(text[i + window_size])

    return inputs, outputs


# TODO build the required RNN model:
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss
from keras.layers import Activation
def build_part2_RNN(window_size, num_chars):
    rnn_model2 = Sequential()
    rnn_model2.add(LSTM(200, input_shape=(window_size, num_chars)))
    rnn_model2.add(Dense(num_chars))
    rnn_model2.add(Activation("softmax"))
    return rnn_model2
