# Example 4.18 SimpleRNN.py
import numpy as np
import tensorflow as tf

i = 4
sequence_length = 5
n = 1
inputs = np.random.random([i, sequence_length, n]).astype(np.float32)
simple_rnn = tf.keras.layers.SimpleRNN(i)
print(inputs)
output = simple_rnn(inputs)
print(output)
