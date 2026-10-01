# Exercise 4.17 - Visualize feature maps from selected VGG19 convolution layers
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model

image_path = Path('Elephant.jpg')
if not image_path.is_file():
    raise SystemExit(f'Image file not found: {image_path}')

base_model = VGG19()
img = load_img(image_path, target_size=(224, 224))
image_batch = np.expand_dims(img_to_array(img), axis=0)
image_batch = preprocess_input(image_batch)

# Indices 2, 3, and 4 select the second, third, and fourth convolutional layers.
for layer_index in (2, 3, 4):
    layer = base_model.layers[layer_index]
    feature_model = Model(inputs=base_model.inputs, outputs=layer.output)
    feature_maps = feature_model.predict(image_batch, verbose=0)
    print(layer_index, layer.name, 'feature maps:', feature_maps.shape)

    column_count = 8
    displayed_count = min(feature_maps.shape[3], 64)
    row_count = (displayed_count + column_count - 1) // column_count
    plt.figure(figsize=(14, 14))
    for feature_index in range(displayed_count):
        axis = plt.subplot(row_count, column_count, feature_index + 1)
        axis.set_xticks([])
        axis.set_yticks([])
        plt.imshow(feature_maps[0, :, :, feature_index], cmap='gray')
    plt.suptitle(f'Feature maps: {layer.name}')
    plt.show()
