# Example 4.20 - SimpleRNN3A.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN


def convert_to_matrix(data, step):
    inputs, targets = [], []
    for index in range(len(data) - step):
        inputs.append(data[index:index + step,])
        targets.append(data[index + step,])
    return np.array(inputs), np.array(targets)


# Requires an internet connection to download the airline passenger data.
data_url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
data_frame = pd.read_csv(data_url, usecols=[1], engine='python')
plt.plot(data_frame)
plt.show()

step = 4
sample_count = data_frame.shape[0]
training_count = int(sample_count * 0.8)
values = data_frame.values
train, test = values[0:training_count, :], values[training_count:sample_count, :]

# Extend each split by the last value to form the final sequences.
test = np.append(test, np.repeat(test[-1,], step))
train = np.append(train, np.repeat(train[-1,], step))
train_x, train_y = convert_to_matrix(train, step)
test_x, test_y = convert_to_matrix(test, step)
train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

model = Sequential()
model.add(SimpleRNN(units=32, input_shape=(1, step), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='rmsprop')
model.summary()
model.fit(train_x, train_y, epochs=10, batch_size=16, verbose=2)

train_prediction = model.predict(train_x)
test_prediction = model.predict(test_x)
predicted = np.concatenate((train_prediction, test_prediction), axis=0)
train_score = model.evaluate(train_x, train_y, verbose=0)
print(train_score)

plt.plot(data_frame, label='Data')
plt.plot(predicted, label='Prediction')
plt.axvline(data_frame.index[training_count], color='red')
plt.legend()
plt.show()
