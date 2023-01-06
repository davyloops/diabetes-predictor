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

    # generate_education_graph(data)
    # generate_age_graph(data)
    # generate_genhlth_graph(data)
    generate_bmi_graph(data)
    # generate_highbp_graph(data)
    # generate_physactivity_graph(data)


def save_graph(graph, name):
    ggsave(plot=graph, filename=name + ".png", dpi=150)


def generate_education_graph(data):
    ordered_categories = ['No School / Kindergarten', 'Elementary School / Middle School', 'High School (Not Finished)', 'High School / GED', 'College (Not Finished)', 'College Graduate']
    graph = (
       ggplot(data, aes(x="Education", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by Education")
        + xlab("Education")
        + ylab("Number of People")
        + scale_x_discrete(limits=ordered_categories)
        + theme(axis_text_x=element_text(rotation=0, hjust=0.3), legend_position = (.8, .2), legend_title=element_blank())
        + coord_flip()
    )
    return save_graph(graph, "education_graph") 


def generate_age_graph(data):
    graph = (
       ggplot(data, aes(x="Age", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(name='', values=[blue, orange], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by Age")
        + xlab("Age")
        + ylab("Number of People")
        + theme(axis_text_x=element_text(rotation=90, hjust=0.3), legend_position = (.275, .77), legend_title=element_blank())
    )
    return save_graph(graph, "age_graph")


def generate_highbp_graph(data):
    graph = (
       ggplot(data, aes(x="HighBP", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by Blood Pressure")
        + xlab("Has High Blood Pressure")
        + ylab("Number of People")
        + theme(axis_text_x=element_text(rotation=90, hjust=0.3), legend_position = (.78, .78), legend_title=element_blank())
    )
    return save_graph(graph, "highbp_graph")


def generate_physactivity_graph(data):
    graph = (
       ggplot(data, aes(x="PhysActivity", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by Physical Activity")
        + xlab("Engages in Physical Activity At Least Once A Month")
        + ylab("Number of People")
        + theme(axis_text_x=element_text(rotation=90, hjust=0.3), legend_position = (.25, .78), legend_title=element_blank())
    )
    return save_graph(graph, "physactivity_graph")


def generate_bmi_graph(data):
    data = data[data['BMI'] <= 55]

    graph = (
    ggplot(data, aes(x="BMI", fill='HasDiabetes'))
    + geom_histogram(binwidth=5, color=gray)
    + scale_fill_manual(values=[blue, orange], labels=['Non-diabetic', 'Diabetic'])
    + guides(fill=guide_legend(ncol=1))
    + ggtitle("Incidence of Diabetes by BMI")
    + xlab("BMI")
    + ylab("Number of People")
    + theme(axis_text_x=element_text(rotation=0, hjust=0.3), legend_position = (.765, .77), legend_title=element_blank())
    )
    return save_graph(graph, "bmi_graph") 


def generate_genhlth_graph(data):
    ordered_categories = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
    graph = (
       ggplot(data, aes(x="GenHlth", fill="HasDiabetes"))
        + geom_bar(color=gray)
        + scale_fill_manual(values=[blue, orange], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by General Health")
        + xlab("General Health")
        + ylab("Number of People")
        + scale_x_discrete(limits=ordered_categories)
        + theme(axis_text_x=element_text(rotation=0, hjust=0.3), legend_position = (.8, .2), legend_title=element_blank())
        + coord_flip()
    )
    return save_graph(graph, "genhlth_graph") 

generate_graphs()