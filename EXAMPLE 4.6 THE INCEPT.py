# Example 4.6
from tensorflow.keras.applications import inception_v3

# Initialize the model with ImageNet weights
model = inception_v3.InceptionV3(weights='imagenet')
print(model.summary())
