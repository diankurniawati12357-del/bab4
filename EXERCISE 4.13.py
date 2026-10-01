# Exercise 4.13 - Select different Image-Classifier models to compare
# Install dependency with: pip install image-classifiers
import cv2
import numpy as np
from keras.applications.imagenet_utils import decode_predictions
from classification_models.keras import Classifiers

# Change this setting to compare the supported architectures.
model_name = 'vgg16'  # resnet50, mobilenetv2, densenet201, inceptionv3
image_size = 299 if model_name == 'inceptionv3' else 224
try:
    classifier, preprocess_input = Classifiers.get(model_name)
except ImportError as error:
    raise SystemExit('Install the dependency with: pip install image-classifiers') from error

model = classifier(input_shape=(image_size, image_size, 3), weights='imagenet', classes=1000)
model.summary()
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print('Webcam is unavailable.')
else:
    try:
        while camera.isOpened():
            ret, cam_frame = camera.read()
            if not ret:
                print('Could not read a frame from the webcam.')
                break
            frame = cv2.resize(cam_frame, (image_size, image_size))
            image_batch = np.expand_dims(np.asarray(frame), axis=0)
            predictions = model.predict(preprocess_input(image_batch), verbose=0)
            label = decode_predictions(predictions, top=1)[0][0]
            cv2.putText(cam_frame, f'{model_name}: {label[1]}, {label[2]:.1%}',
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.imshow('Classification', cam_frame)
            if cv2.waitKey(30) == 27:
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
