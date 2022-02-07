import joblib
import pandas as pd
import numpy as np
# from alibi_detect.utils.saving import load_detector
import json


import joblib


class Predictor(object):

    def __init__(self):
        self.model = joblib.load('CustomerChurnPredictor.sav')

    def predict(self, X, features_names):
        prediction = self.model.predict_proba(X)
                                              
        class_name = ['Not Churn', 'Churn']                                             
        predicted_class =   class_name[np.argmax(prediction)]                                   
        print('Predicted Class name: ', predicted_class)
        predicted_class_prob = str(np.max(prediction))
        print('Predicted class Certainty: ', predicted_class_prob)
        json_results = {"Predicted Class": predicted_class, "Predicted Certainty Score":predicted_class_prob}

        return json_results