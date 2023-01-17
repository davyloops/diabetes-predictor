import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import pickle
import os.path

def prepare_data():
    data = pd.read_csv("diabetes_dataset.csv")
    data.drop(["CholCheck", "HvyAlcoholConsump", "AnyHealthcare", "Stroke", "NoDocbcCost", "HeartDiseaseorAttack"], axis=1, inplace=True)
    data.rename({"Diabetes_binary": "target"}, axis=1, inplace=True)
    return data


def fit_model(X_train, y_train):
    model = SGDClassifier(max_iter=1000000, loss="perceptron")
    model.fit(X_train, y_train)
    return model


def score_model(model, X_test, y_test):
    y_preds = model.predict(X_test)
    score = accuracy_score(y_test, y_preds)
    print(score)

    
def save_model(model):
    model_filename = 'model.pkl'
    if os.path.isfile(model_filename):
        return
    pickle.dump(model, open(model_filename, 'wb'))


def create_model():
    data = prepare_data()

    X = data.drop("target", axis=1)
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = fit_model(X_train, y_train)
    score_model(model, X_test, y_test)
    save_model(model)


def predict(answers):
    model = pickle.load(open('model.pkl', 'rb'))
    answers_int = []

    for answer in answers:
        answers_int.append(int(answer))

    answers = np.array(answers_int)
    prediction = model.predict(answers.reshape(1, -1))
    prediction = int(prediction[0])
    return prediction