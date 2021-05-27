# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:54:17 2021

@author: shubh
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return ("Hello")

if __name__ == '__main__':
    app.run()
