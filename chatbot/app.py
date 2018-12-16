from flask import Flask, request, make_response, jsonify
import json
from sklearn.externals import joblib
import numpy as np
import os
from recommender import user_features,make_query

# initialize the flask app
app = Flask(__name__)

def make_recommendations():
    pass

# default route
@app.route('/')
def index():
    return 'Hello World!'
# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    req = request.get_json(force=True)
    action = req.get("queryResult").get("action")
    parameters = req.get("queryResult").get("parameters")
    query = make_query(user_features(parameters))
    full_dir = "knn.pickle"
    model = joblib.load(os.path.realpath(full_dir))
    query = np.array(query)
    print(query)
    result = model.kneighbors(query.reshape(1,-1))
    print(result)
    return make_response(jsonify({'fulfillmentText': str(result)}))
# run the app
if __name__ == '__main__':
   app.run()