import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.efficientnet_v2 import (EfficientNetV2L,
                                                           decode_predictions)

# from tensorflow.keras.applications.resnet50 import (
#     ResNet50,
#     decode_predictions,
#     preprocess_input,
# )


image = tf.keras.preprocessing.image.load_img("./giraffe.jpg")
input_arr = tf.keras.preprocessing.image.img_to_array(image)

# If using ResNet50, use this line:
# input_arr = tf.image.resize(input_arr, (224, 224))

# If using EfficientNetV2L, use this line:
input_arr = tf.image.resize(input_arr, (480, 480))

input_arr = np.array([input_arr])

# model = ResNet50()
model = EfficientNetV2L()

predictions = decode_predictions(model.predict(input_arr))

for _, label, prob in predictions[0]:
  print(f"{label}: {prob}")
