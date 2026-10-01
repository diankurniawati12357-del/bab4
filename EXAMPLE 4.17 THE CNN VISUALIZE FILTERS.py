# Example 4.17 - CNN Visualize Filters, combined parts 1-6
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model

# Load VGG19 and display its layers
# PART 1
model = VGG19()
model.summary()
for layer_index, layer in enumerate(model.layers):
    print(layer_index, layer.name)

# Show filter and bias shapes for convolutional layers
# PART 2
for layer_index, layer in enumerate(model.layers):
    if 'conv' in layer.name:
        filters, biases = layer.get_weights()
        print(layer_index, layer.name, filters.shape, biases.shape)

# Display the first four filters from the first convolutional layer
# PART 3
layer_index = 1
filters, biases = model.layers[layer_index].get_weights()
filter_shape = filters.shape
print('Color channels:', filter_shape[2])
print('Filter size:', filter_shape[0], filter_shape[1])
print('Total number of filters:', filter_shape[3])
filter_min, filter_max = filters.min(), filters.max()
if filter_max > filter_min:
    filters = (filters - filter_min) / (filter_max - filter_min)

number_of_filters = 4
plot_index = 1
plt.figure(figsize=(10, 10))
for filter_index in range(number_of_filters):
    current_filter = filters[:, :, :, filter_index]
    for channel_index in range(filter_shape[2]):
        axis = plt.subplot(number_of_filters, filter_shape[2], plot_index)
        axis.set_xticks([])
        axis.set_yticks([])
        plt.imshow(current_filter[:, :, channel_index], cmap='gray')
        plot_index += 1
plt.show()


# PART 4
def plot_feature_maps(feature_maps):
    column_count = 8
    row_count = int(np.ceil(feature_maps.shape[3] / column_count))
    plt.figure(figsize=(20, 20))
    for feature_index in range(feature_maps.shape[3]):
        axis = plt.subplot(row_count, column_count, feature_index + 1)
        axis.set_xticks([])
        axis.set_yticks([])
        plt.imshow(feature_maps[0, :, :, feature_index], cmap='gray')
    plt.show()


# Select the hidden layer to visualize
# PART 5
layer_index = 1
feature_model = Model(inputs=model.inputs, outputs=model.layers[layer_index].output)
feature_model.summary()

# PART 6
img_path = Path('Elephant.jpg')
if not img_path.is_file():
    print(f'Image file not found: {img_path}; filter plots above are still available.')
else:
    img = load_img(img_path, target_size=(224, 224))
    image_batch = np.expand_dims(img_to_array(img), axis=0)
    image_batch = preprocess_input(image_batch)
    feature_maps = feature_model.predict(image_batch)
    print('Feature maps:', feature_maps.shape)
    plot_feature_maps(feature_maps)
