# Exercise 4.8 - Compare MNIST CNN with one and two convolution blocks
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape((-1, 28, 28, 1)).astype('float32') / 255.0
X_test = X_test.reshape((-1, 28, 28, 1)).astype('float32') / 255.0
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


def build_model(use_second_block):
    model = Sequential()
    model.add(Conv2D(32, (5, 5), input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPooling2D())
    model.add(Dropout(0.2))
    if use_second_block:
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D())
        model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


for use_second_block in (False, True):
    model = build_model(use_second_block)
    model.fit(X_train, y_train, validation_data=(X_test, y_test),
              epochs=10, batch_size=200, verbose=0)
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    label = 'two convolution blocks' if use_second_block else 'one convolution block'
    print(f'{label}: loss={loss:.4f}, accuracy={accuracy:.4f}')
