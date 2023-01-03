import pickle
import numpy as np

def predict(answers):
    model = pickle.load(open('model.pkl', 'rb'))
    answers_int = []
    for answer in answers:
        answers_int.append(int(answer))
    answers = np.array(answers_int)
    prediction = model.predict(answers.reshape(1, -1))
    prediction = int(prediction[0])
    return prediction