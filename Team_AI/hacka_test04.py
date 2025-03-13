import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense,Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

df = pd.read_excel('kokumotu.xlsx')
subset = (np.asarray(df.iloc[0:])).transpose()
print(subset)
print(subset.shape)
sequence_length = 9
num_sequences = 1
hidden_units = 32
X = subset[1:, :-1].reshape(-1, sequence_length, 1)
y = subset[1:, 1:].reshape(-1, sequence_length, 1)
print(X)
scaler = MinMaxScaler()
X = scaler.fit_transform(X.reshape(-1, 1)).reshape(-1, sequence_length, 1)
y = scaler.transform(y.reshape(-1, 1)).reshape(-1, sequence_length, 1)


model = Sequential()
model.add(LSTM(64, input_shape=(sequence_length, 1),return_sequences=True))
model.add(LSTM(128))
model.add(Dropout(0.25))
model.add(Dense(sequence_length))


model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

model.fit(X, y, epochs=200, batch_size=1)

prediction = model.predict(X[:1])

print(scaler.inverse_transform(prediction.reshape(-1, 1)).reshape(1, sequence_length, 1))
print((scaler.inverse_transform(prediction.reshape(-1, 1)).reshape(1, sequence_length, 1)).shape)