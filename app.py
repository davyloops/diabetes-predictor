from flask import Flask, request, render_template, redirect, url_for
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from model import predict
from graphs import generate_graphs

app = Flask(__name__)
answers = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questionnaire', methods =["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        height_feet = int(request.form.get("height-feet"))
        height_inches = int(request.form.get("height-inches"))
        height = height_feet * 12 + height_inches
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
        # answers = [request.form.get("highbp"), request.form.get("highchol"), bmi, request.form.get("smoker"), request.form.get("physactivity"), 
        # request.form.get("fruits"), request.form.get("veggies"), request.form.get("genhlth"), request.form.get("menthlth"), request.form.get("physhlth"),
        # request.form.get("diffwalk"), request.form.get("sex"), request.form.get("age"), request.form.get("education"), request.form.get("income")]

        return redirect(url_for('prediction'))
    return render_template('questionnaire.html')


@app.route('/prediction')
def prediction():
    prediction = predict(list(answers.values()))
    # prediction = predict(answers)
    graphs = generate_graphs(answers)
    return render_template('prediction.html', prediction=prediction, education_graph=graphs["education"], age_graph=graphs["age"], genhlth_graph=graphs["genhlth"], bmi_graph=graphs["bmi"])

if __name__ == "__main__":
    app.run(debug=True)