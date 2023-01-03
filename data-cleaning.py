# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 15:29:27 2022

@author: David
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

    
def plot_feature_importances():
    importances = model.feature_importances_
    sorted_indices = np.argsort(importances)[::-1]
    plt.title('Feature Importance')
    plt.bar(range(X_train.shape[1]), importances[sorted_indices], align='center')
    plt.xticks(range(X_train.shape[1]), X_train.columns[sorted_indices], rotation=90)
    plt.tight_layout()
    plt.show()
    
def save_model():
    pickle.dump(model, open('model.pkl', 'wb'))


data = pd.read_csv("diabetes_dataset.csv")
data.drop(["CholCheck", "HvyAlcoholConsump", "AnyHealthcare", "Stroke", "NoDocbcCost", "HeartDiseaseorAttack"], axis=1, inplace=True)
data.rename({"Diabetes_binary": "target"}, axis=1, inplace=True)

X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)
toPredict = np.array([1, 1, 33, 1, 0, 1, 1, 5, 30, 30, 1, 0, 9, 5, 1])
prediction = model.predict(toPredict.reshape(1, -1))
print(prediction)
# =============================================================================
# y_preds = model.predict(X_test)
# score = accuracy_score(y_test, y_preds)
# plot_feature_importances()
# save_model()
# =============================================================================
