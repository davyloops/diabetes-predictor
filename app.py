from flask import Flask, request, render_template, redirect, url_for
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from model import predict
from datetime import datetime

app = Flask(__name__)
answers = None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questionnaire', methods =["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        height = int(request.form.get("height-feet")) * 12 + int(request.form.get("height-inches"))
        weight = int(request.form.get("weight"))
        bmi = str(int(weight * 703 / height**2))

        global answers
        answers = {
            "HighBP": request.form.get("highbp"),
            "HighChol": request.form.get("highchol"),
            "BMI": bmi,
            "Smoker": request.form.get("smoker"),
            "PhysActivity": request.form.get("physactivity"),
            "Fruits": request.form.get("fruits"),
            "Veggies": request.form.get("veggies"),
            "GenHlth": request.form.get("genhlth"),
            "MentHlth": request.form.get("menthlth"),
            "PhysHlth": request.form.get("physhlth"),
            "DiffWalk": request.form.get("diffwalk"),
            "Sex": request.form.get("sex"),
            "Age": request.form.get("age"),
            "Education": request.form.get("education"),
            "Income": request.form.get("income")
        }

        return redirect(url_for('prediction'))
    return render_template('questionnaire.html')


@app.route('/prediction')
def prediction():
    if answers != None:
        prediction = predict(list(answers.values()))
        return render_template('prediction.html', prediction=prediction)

    return render_template('prediction.html')


@app.errorhandler(Exception)
def error(e):
    error_log = open("error_log.txt","a")
    error_log.write(f"Error: {str(e)}, Time: {datetime.now()} \n")
    error_log.close()

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)