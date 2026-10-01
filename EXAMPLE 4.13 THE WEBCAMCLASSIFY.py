# Example 4.13
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import vgg16

image_size = 224
model = vgg16.VGG16(weights='imagenet')
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

            frame = cv2.resize(cam_frame, (image_size, image_size))
            image_batch = np.expand_dims(img_to_array(frame), axis=0)
            processed_image = vgg16.preprocess_input(image_batch.copy())
            predictions = model.predict(processed_image, verbose=0)
            label = decode_predictions(predictions, top=1)[0][0]
            cv2.putText(cam_frame, f'VGG16: {label[1]}, {label[2]:.1%}',
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (255, 0, 0), 2)
            cv2.imshow('video image', cam_frame)
            if cv2.waitKey(30) == 27:
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
