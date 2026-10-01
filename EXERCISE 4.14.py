# Exercise 4.14 - Select a webcam classifier with if/elif statements
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import vgg16, resnet50, mobilenet, inception_v3

model_name = input('Choose vgg16, resnet50, mobilenet, or inception_v3: ').strip().lower()
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
    raise SystemExit('Unsupported model name.')

print(model.summary())
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print('Webcam is unavailable.')
else:
    try:
        while camera.isOpened():
            ok, cam_frame = camera.read()
            if not ok:
                print('Could not read a frame from the webcam.')
                break
            image_batch = np.expand_dims(
                img_to_array(cv2.resize(cam_frame, (image_size, image_size))), axis=0
            )
            predictions = model.predict(preprocess(image_batch), verbose=0)
            label = decode_predictions(predictions, top=1)[0][0]
            cv2.putText(cam_frame, f'{model_name}: {label[1]}, {label[2]:.1%}',
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.imshow('video image', cam_frame)
            if cv2.waitKey(30) == 27:
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
