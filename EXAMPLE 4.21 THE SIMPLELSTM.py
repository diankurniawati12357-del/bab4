# Example 4.21 SimpleLSTM.py
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    keras.Input(shape=(None,), dtype='int32'),
    layers.Embedding(input_dim=100, output_dim=32),
    layers.LSTM(64),
    layers.Dense(1),
])
model.summary()
