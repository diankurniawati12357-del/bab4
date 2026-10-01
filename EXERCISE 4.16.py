# Exercise 4.16 - Display all filters from the first VGG19 convolution layer
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg19 import VGG19

model = VGG19()
layer_index = 1
layer = model.layers[layer_index]
filters, biases = layer.get_weights()
filter_count = filters.shape[3]
channel_count = filters.shape[2]
print(layer_index, layer.name, filters.shape, biases.shape)

filter_min, filter_max = filters.min(), filters.max()
if filter_max > filter_min:
    filters = (filters - filter_min) / (filter_max - filter_min)

column_count = 8
row_count = (filter_count * channel_count + column_count - 1) // column_count
plt.figure(figsize=(16, 16))
plot_index = 1
for filter_index in range(filter_count):
    for channel_index in range(channel_count):
        axis = plt.subplot(row_count, column_count, plot_index)
        axis.set_xticks([])
        axis.set_yticks([])
        plt.imshow(filters[:, :, channel_index, filter_index], cmap='gray')
        plot_index += 1
plt.suptitle(f'All {filter_count} filters, by color channel: {layer.name}')
plt.show()
