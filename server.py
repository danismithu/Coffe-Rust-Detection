# -*- coding: utf-8 -*-
"""
COFFEE RUST DETECTION
Created on Sun Oct  6 21:48:45 2019
@author: Daniel Smith
"""

from flask import Flask, render_template, request

import tensorflow as tf
from keras.applications.imagenet_utils import preprocess_input
from keras.preprocessing import image

from tensorflow.python.keras.backend import set_session

import numpy as np

import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import MethodNotAllowed

import stripe
import gunicorn
import PIL


app = Flask(__name__, template_folder='view')

global classes
global graph
global model
global sess

classes = ['Healthy', 'Red spider mite', 'Rust level 1', 'Rust level 2', 'Rust level 3', 'Rust level 4']
model_name = './model/coffee_rust_model.h5'

#--------------------- Stripe ------------------
stripe_keys = {
        'secret_key': os.environ.get('STRIPE_SECRET_KEY', None),
        'publishable_key': os.environ.get('STRIPE_PUBLISHABLE_KEY', None)
    }

stripe.api_key = stripe_keys['secret_key']

#------------------- Tensorflow ---------------
sess = tf.Session()

graph = tf.get_default_graph()
set_session(sess)

model = tf.keras.Sequential(
            [
                tf.keras.applications.MobileNetV2(weights="imagenet", input_shape=(224, 224, 3), include_top=False),
                tf.keras.layers.GlobalAveragePooling2D(),
                tf.keras.layers.Dense(256, activation="relu", name="descriptor"),
                tf.keras.layers.Dense(6, activation="softmax", name="probs"),
            ]
        )
model.load_weights(model_name)

print('Model loaded!')

def model_predict(img_path, model_loaded):
    img = image.load_img(img_path, target_size=(224, 224))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='caffe')

    with graph.as_default():
        model_loaded._make_predict_function()
        set_session(sess)
        preds = model_loaded.predict(x)

    return preds


@app.route('/', methods=['GET'])
def main():
   return(render_template('main.html', key=stripe_keys['publishable_key']))


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'GET':
        return render_template('error.html')

    try:
        amount = 75
        customer = stripe.Customer.create(
                email=request.form['stripeEmail'],
                source=request.form['stripeToken']
            )

        stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='usd',
                description='Coffee Rust membership'
            )

        return render_template('analyze.html')

    except stripe.error.StripeError as e:
        print('Stripe error: ' + str(e))
        return render_template('error.html')
    except MethodNotAllowed as e:
        print('Method error: ' + str(e))
        return render_template('error.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)

        preds_class = preds.argmax()

        result = classes[preds_class]
        return result

    return None

if __name__ == '__main__':
    app.run()
