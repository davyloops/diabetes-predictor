import pandas as pd
from plotnine import *

blue = '#8DA0CB'
orange = '#FC8D62'
gray = '#5A5A5A'

def prepare_data():
    data = pd.read_csv('prepared_data.csv')
    return data


def generate_graphs():
    data = prepare_data()

    generate_education_graph(data)
    generate_age_graph(data)
    generate_genhlth_graph(data)
    generate_bmi_graph(data)


def save_graph(graph, name):
    ggsave(plot=graph, filename=name + ".png", dpi=150)


def generate_education_graph(data):
    ordered_categories = ['No School / Kindergarten', 'Elementary School / Middle School', 'High School (Not Finished)', 'High School / GED', 'College (Not Finished)', 'College Graduate']
    graph = (
       ggplot(data, aes(x="Education", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange])
        + scale_x_discrete(limits=ordered_categories)
        + theme(axis_text_x=element_text(rotation=0, hjust=0.3))
        + coord_flip()
    )
    return save_graph(graph, "education_graph") 


def generate_age_graph(data):
    graph = (
       ggplot(data, aes(x="Age", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange])
        + theme(axis_text_x=element_text(rotation=90, hjust=0.3))
    )
    return save_graph(graph, "age_graph") 


def generate_bmi_graph(data):
    data = data[data['BMI'] <= 55]

    graph = (
    ggplot(data, aes(x="BMI", fill='HasDiabetes'))
    + geom_histogram(binwidth=5, color=gray)
    + scale_fill_manual(values=[blue, orange])
    + theme(axis_text_x=element_text(rotation=0, hjust=0.3))
    )
    return save_graph(graph, "bmi_graph") 


def generate_genhlth_graph(data):
    ordered_categories = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
    graph = (
       ggplot(data, aes(x="GenHlth", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange])
        + scale_x_discrete(limits=ordered_categories)
        + theme(axis_text_x=element_text(rotation=0, hjust=0.3))
        + coord_flip()
    )
    return save_graph(graph, "genhlth_graph") 