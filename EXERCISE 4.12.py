# Exercise 4.12 - Add DenseNet to webcam image classification
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.densenet import DenseNet201, preprocess_input

model = DenseNet201(weights='imagenet')
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
            image_batch = np.expand_dims(img_to_array(cv2.resize(cam_frame, (224, 224))), axis=0)
            predictions = model.predict(preprocess_input(image_batch), verbose=0)
            label = decode_predictions(predictions, top=1)[0][0]
            cv2.putText(cam_frame, f'DenseNet201: {label[1]}, {label[2]:.1%}',
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.imshow('video image', cam_frame)
            if cv2.waitKey(30) == 27:
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
