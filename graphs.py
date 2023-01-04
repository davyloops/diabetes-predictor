import pandas as pd
import numpy as np
from plotnine import *
import io
import base64
import matplotlib.pyplot as plt

blue = '#8DA0CB'
orange = '#FC8D62'
gray = '#5A5A5A'

def prepare_data():
    data = pd.read_csv('prepared_data.csv')
    data = data.sample(frac=0.03)
    return data


def generate_graphs(answers):
    data = prepare_data()

    graphs = {}
    graphs["education"] = generate_education_graph(data)
    graphs["age"] = generate_age_graph(data, answers)
    graphs["genhlth"] = generate_genhlth_graph(data)
    graphs["bmi"] = generate_bmi_graph(data)

    return graphs


def save_graph(graph):
    buffer = io.BytesIO()
    ggsave(plot=graph, filename=buffer, dpi=150)
    return base64.b64encode(buffer.getbuffer()).decode("utf-8")


def generate_education_graph(data):
    data_modified = data[['Education','HasDiabetes']]

    ordered_categories = ['No School / Kindergarten', 'Elementary School / Middle School', 'High School (Not Finished)', 'High School / GED', 'College (Not Finished)', 'College Graduate']
    graph = (
       ggplot(data_modified, aes(x="Education", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange])
        + scale_x_discrete(limits=ordered_categories)
        + theme(axis_text_x=element_text(rotation=0, hjust=0.3))
        + coord_flip()
    )
    return save_graph(graph) 


def generate_age_graph(data, answers):
    data_modified = data[['Age','HasDiabetes']]
    age_category = np.sort(data_modified["Age"].unique())[int(answers["Age"]) - 1]

    graph = (
       ggplot(data_modified, aes(x="Age", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + annotate('text', x=age_category, y = 1000, label='You', angle=90)
        + scale_fill_manual(values=[blue, orange])
        + theme(axis_text_x=element_text(rotation=90, hjust=0.3))
    )
    return save_graph(graph) 


def generate_bmi_graph(data):
    data_modified = data[data['BMI'] <= 55]
    data_modified = data_modified[['BMI','HasDiabetes']]

    graph = (
    ggplot(data_modified, aes(x="BMI", fill='HasDiabetes'))
    + geom_histogram(binwidth=5, color=gray)
    + scale_fill_manual(values=[blue, orange])
    + theme(axis_text_x=element_text(rotation=0, hjust=0.3))
    )

    return save_graph(graph) 


def generate_genhlth_graph(data):
    data_modified = data[['GenHlth','HasDiabetes']]

    ordered_categories = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
    graph = (
       ggplot(data_modified, aes(x="GenHlth", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange])
        + scale_x_discrete(limits=ordered_categories)
        + theme(axis_text_x=element_text(rotation=0, hjust=0.3))
        + coord_flip()
    )
    return save_graph(graph) 