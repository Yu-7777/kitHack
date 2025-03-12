import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense,Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd
import numpy as np
df = pd.read_excel('hack_data01.xlsx')
subset=(np.asarray(df.iloc[0:])).transpose()


