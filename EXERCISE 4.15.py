# Exercise 4.15 - Visualize filters from the second convolution layer
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg19 import VGG19

model = VGG19()
layer_index = 2
layer = model.layers[layer_index]
filters, biases = layer.get_weights()
print(layer_index, layer.name, filters.shape, biases.shape)

# Display all input-channel slices for the first filter of this layer.
selected_filter = filters[:, :, :, 0]
channel_count = selected_filter.shape[2]
column_count = 8
row_count = (channel_count + column_count - 1) // column_count
plt.figure(figsize=(12, 12))
for channel_index in range(channel_count):
    axis = plt.subplot(row_count, column_count, channel_index + 1)
    axis.set_xticks([])
    axis.set_yticks([])
    plt.imshow(selected_filter[:, :, channel_index], cmap='gray')
plt.suptitle(f'Filter 0 input channels: {layer.name}')
plt.show()
