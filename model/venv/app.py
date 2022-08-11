from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import joblib
#from model import NLPModel

app = Flask(__name__)
api = Api(app)


classifier = joblib.load('model2.h5')

with open('set_scaler.pkl', 'rb') as file:
    # Call load method to deserialze
    sc = pickle.load(file)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']

        # vectorize the user's query and make a prediction
        uq_vectorized = classifier.vectorizer_transform(np.array([user_query]))
        prediction = classifier.predict(uq_vectorized)
        pred_proba = classifier.predict_proba(uq_vectorized)

        # Output either 'Negative' or 'Positive' along with the score
        if prediction == 0:
            print("Stage 0")
        elif prediction == 1:
            print("Stage 1")
        elif prediction == 2:
            print("Stage 2")
        elif prediction == 3:
            print("Stage 3")
        elif prediction == 4:
            print("Stage 4")
        elif prediction == 5:
            print("Stage 5")
        else:
            print("Error")

        # round the predict proba value and set to new variable
        confidence = round(pred_proba[0], 3)

        # create JSON object
        output = {'prediction': prediction, 'confidence': confidence}

        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(debug=True)
