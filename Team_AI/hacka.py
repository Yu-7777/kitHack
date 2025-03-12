import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

import pandas as pd
import numpy as np

df = pd.read_excel('hack_data01.xlsx')
subset = np.asarray(df.iloc[0:])

sequence_length = 12
num_sequences = 1
hidden_units = 32


X = subset[0][:12].reshape(1, sequence_length, 1)
y = subset[0][1:13].reshape(1, sequence_length, 1)
x=X/sum(X)
y=y/sum(y)

model = Sequential()
model.add(LSTM(hidden_units, input_shape=(sequence_length, 1)))
model.add(Dense(1))

model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

model.fit(X, y, epochs=100, batch_size=1)