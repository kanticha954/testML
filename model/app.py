import pickle
import numpy as np
import joblib
import os

from flask import Flask, render_template, request

app = Flask(__name__)

classifier = joblib.load('model.pkl')
print("Enter the following details to make the predictions:- n")



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def getPredict():
    resistance_thumb = request.form['resistance_thumb']
    bend_thumb = request.form['bend_thumb']
    resistance_index = request.form['resistance_index']
    bend_index = request.form['bend_index']
    resistance_mid = request.form['resistance_mid']
    bend_mid = request.form['bend_mid']
    resistance_ring = request.form['resistance_ring']
    bend_ring = request.form['bend_ring']
    resistance_little = request.form['resistance_little']
    bend_little = request.form['bend_little']
    
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    
    XTest = np.array([[resistance_thumb, bend_thumb, resistance_index,
                      bend_index, resistance_mid, bend_mid,
                      resistance_ring, bend_ring,
                      resistance_little, bend_little,
                      x, y, z]], dtype=np.float64)

    predicted = classifier.predict(XTest)[0]
    predicted = 1 / (1 + np.exp(-predicted))
    return render_template('index.html',
    prediction_text = f'Predicted: {predicted * 100:.2f}%')

if __name__ == '__main__':
    app.run(debug = True)