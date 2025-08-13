import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from tensorflow.keras.applications.efficientnet import preprocess_input

# Load the trained ResNet50 model (cached for performance) preprocess_input
@st.cache_resource
def load_model(model_path="updated_model.h5"):
    model = tf.keras.models.load_model(model_path)
    return model

# Preprocess the image for ResNet50
def preprocess_image(img_path, target_size=(224, 224)):
    def load_and_preprocess_test(path):
        img = load_img(path.numpy().decode(), target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = preprocess_input(img_array)
        return img_array

    def tf_load_and_preprocess_test(path):
        img = tf.py_function(load_and_preprocess_test, [path], [tf.float32])
        img[0].set_shape((224, 224, 3))
        return img[0]

    def create_test_dataset(paths):
        ds = tf.data.Dataset.from_tensor_slices(paths)
        ds = ds.map(tf_load_and_preprocess_test, num_parallel_calls=tf.data.AUTOTUNE)
        ds = ds.batch(32).prefetch(tf.data.AUTOTUNE)
        return ds

    test_ds = create_test_dataset(paths=[img_path])
    return test_ds


# Predict Dog category and confidence scores
def predict_fish(model, img_array, class_names):
    preds = model.predict(img_array)
    predicted_index = np.argmax(preds)
    confidence = preds[0][predicted_index] * 100
    return class_names[predicted_index], confidence, preds[0]
