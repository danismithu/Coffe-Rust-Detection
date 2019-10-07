# -*- coding: utf-8 -*-
"""
COFFEE RUST DETECTION
Created on Sun Oct  6 21:48:45 2019
@author: Daniel Smith
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'