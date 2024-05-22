import tensorflow as tf
import numpy as np

img = np.load('00new_img.npy')

model = tf.keras.models.load_model('mnist_digit_recognizer.h5')

all_predictions = model.predict(img)

final_prediction = np.argmax(all_predictions)

print(f'Number is {final_prediction}')
