# Example 4.12
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import vgg16, resnet50, mobilenet, inception_v3

# Select one model and its matching preprocessing function
model_name = 'mobilenet'
if model_name == 'vgg16':
    model = vgg16.VGG16(weights='imagenet')
    preprocess = vgg16.preprocess_input
    image_size = 224
elif model_name == 'resnet50':
    model = resnet50.ResNet50(weights='imagenet')
    preprocess = resnet50.preprocess_input
    image_size = 224
elif model_name == 'mobilenet':
    model = mobilenet.MobileNet(weights='imagenet')
    preprocess = mobilenet.preprocess_input
    image_size = 224
elif model_name == 'inception_v3':
    model = inception_v3.InceptionV3(weights='imagenet')
    preprocess = inception_v3.preprocess_input
    image_size = 299
else:
    raise ValueError(f'Unsupported model: {model_name}')

print(model.summary())
img_path = 'Elephant.jpg'
try:
    img = image.load_img(img_path, target_size=(image_size, image_size))
except FileNotFoundError:
    print(f'Image file not found: {img_path}')
else:
    image_batch = np.expand_dims(image.img_to_array(img), axis=0)
    processed_image = preprocess(image_batch.copy())
    predictions = model.predict(processed_image)
    print(decode_predictions(predictions))
