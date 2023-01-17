import pandas as pd
from plotnine import *

BLUE = '#8DA0CB'
ORANGE = '#FC8D62'
GRAY = '#5A5A5A'
PLOT_TITLE_SIZE = 12
AXIS_TITLE_SIZE = 10

def prepare_data():
    data = pd.read_csv('diabetes_dataset.csv')
    data.drop(["CholCheck", "HvyAlcoholConsump", "AnyHealthcare", "Stroke", "NoDocbcCost", "HeartDiseaseorAttack"], axis=1, inplace=True)
    data.rename({"Diabetes_binary": "HasDiabetes"}, axis=1, inplace=True)
    
    # Values are renamed to improve readability of the graphs.
    data["HasDiabetes"].replace(0, "No", inplace=True)
    data["HasDiabetes"].replace(1, "Yes", inplace=True)
    
    data["HighBP"].replace(0, "No", inplace=True)
    data["HighBP"].replace(1, "Yes", inplace=True)
    
    data["HighChol"].replace(0, "No", inplace=True)
    data["HighChol"].replace(1, "Yes", inplace=True)
    
    data["Smoker"].replace(0, "No", inplace=True)
    data["Smoker"].replace(1, "Yes", inplace=True)
    
    data["PhysActivity"].replace(0, "No", inplace=True)
    data["PhysActivity"].replace(1, "Yes", inplace=True)
    
    data["Fruits"].replace(0, "No", inplace=True)
    data["Fruits"].replace(1, "Yes", inplace=True)
    
    data["Veggies"].replace(0, "No", inplace=True)
    data["Veggies"].replace(1, "Yes", inplace=True)
    
    data["Fruits"].replace(0, "No", inplace=True)
    data["Fruits"].replace(1, "Yes", inplace=True)
    
    data["DiffWalk"].replace(0, "No", inplace=True)
    data["DiffWalk"].replace(1, "Yes", inplace=True)
    
    data["Sex"].replace(0, "Male", inplace=True)
    data["Sex"].replace(1, "Female", inplace=True)
    
    data["GenHlth"].replace(1, "Excellent", inplace=True)
    data["GenHlth"].replace(2, "Very Good", inplace=True)
    data["GenHlth"].replace(3, "Good", inplace=True)
    data["GenHlth"].replace(4, "Fair", inplace=True)
    data["GenHlth"].replace(5, "Poor", inplace=True)
    
    data["Age"].replace(1, "18 - 24", inplace=True)
    data["Age"].replace(2, "25 - 29", inplace=True)
    data["Age"].replace(3, "30 - 34", inplace=True)
    data["Age"].replace(4, "35 - 39", inplace=True)
    data["Age"].replace(5, "40 - 44", inplace=True)
    data["Age"].replace(6, "45 - 49", inplace=True)
    data["Age"].replace(7, "50 - 54", inplace=True)
    data["Age"].replace(8, "55 - 59", inplace=True)
    data["Age"].replace(9, "60 - 64", inplace=True)
    data["Age"].replace(10, "65 - 69", inplace=True)
    data["Age"].replace(11, "70 - 74", inplace=True)
    data["Age"].replace(12, "75 - 79", inplace=True)
    data["Age"].replace(13, "80 or older", inplace=True)
    
    data["Education"].replace(1, "No School / Kindergarten", inplace=True)
    data["Education"].replace(2, "Elementary School / Middle School", inplace=True)
    data["Education"].replace(3, "High School (Not Finished)", inplace=True)
    data["Education"].replace(4, "High School / GED", inplace=True)
    data["Education"].replace(5, "College (Not Finished)", inplace=True)
    data["Education"].replace(6, "College Graduate", inplace=True)
    
    data["Income"].replace(1, "Less than 10,000", inplace=True)
    data["Income"].replace(2, "$10,000 - $14,999", inplace=True)
    data["Income"].replace(3, "$15,000 - $19,999", inplace=True)
    data["Income"].replace(4, "$20,000 - $24,999", inplace=True)
    data["Income"].replace(5, "$25,000 - $34,999", inplace=True)
    data["Income"].replace(6, "$35,000 - $49,999", inplace=True)
    data["Income"].replace(7, "$50,000 - $74,999", inplace=True)
    data["Income"].replace(8, "$75,000 or more", inplace=True)
    
    return data


def generate_graphs():
    data = prepare_data()

    generate_age_graph(data)
    generate_bmi_graph(data)
    generate_highbp_graph(data)
    generate_physactivity_graph(data)


def save_graph(graph, name):
    ggsave(plot=graph, filename=name + ".png", dpi=150)


def generate_age_graph(data):
    graph = (
       ggplot(data, aes(x="Age", fill="HasDiabetes"))
        + geom_bar(color=GRAY)
        + scale_fill_manual(name='', values=[BLUE, ORANGE], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by Age")
        + xlab("Age")
        + ylab("Number of People")
        + theme(
            plot_title=element_text(size=PLOT_TITLE_SIZE),
            axis_title=element_text(size=AXIS_TITLE_SIZE),
            axis_text_x=element_text(rotation=90, hjust=0.3), 
            legend_position = (.275, .77), 
            legend_title=element_blank()
            )
    )
    return save_graph(graph, "age_graph")


def generate_highbp_graph(data):
    graph = (
       ggplot(data, aes(x="HighBP", fill="HasDiabetes"))
        + geom_bar(color=GRAY)
        + scale_fill_manual(values=[BLUE, ORANGE], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by Blood Pressure")
        + xlab("Has High Blood Pressure")
        + ylab("Number of People")
        + theme(
            plot_title=element_text(size=PLOT_TITLE_SIZE),
            axis_title=element_text(size=AXIS_TITLE_SIZE),
            axis_text_x=element_text(rotation=90, hjust=0.3), 
            legend_position = (.78, .78), 
            legend_title=element_blank()
            )
    )
    return save_graph(graph, "highbp_graph")


def generate_physactivity_graph(data):
    graph = (
       ggplot(data, aes(x="PhysActivity", fill="HasDiabetes"))
        + geom_bar(color=GRAY)
        + scale_fill_manual(values=[BLUE, ORANGE], labels=['Non-diabetic', 'Diabetic'])
        + guides(fill=guide_legend(ncol=1))
        + ggtitle("Incidence of Diabetes by Physical Activity")
        + xlab("Engages in Physical Activity At Least Once A Month")
        + ylab("Number of People")
        + theme(
            plot_title=element_text(size=PLOT_TITLE_SIZE),
            axis_title=element_text(size=AXIS_TITLE_SIZE),
            axis_text_x=element_text(rotation=90, hjust=0.3), 
            legend_position = (.25, .78), 
            legend_title=element_blank()
            )
    )
    return save_graph(graph, "physactivity_graph")


def generate_bmi_graph(data):
    data = data[data['BMI'] <= 55]

    graph = (
    ggplot(data, aes(x="BMI", fill='HasDiabetes'))
    + geom_histogram(binwidth=5, color=GRAY)
    + scale_fill_manual(values=[BLUE, ORANGE], labels=['Non-diabetic', 'Diabetic'])
    + guides(fill=guide_legend(ncol=1))
    + ggtitle("Incidence of Diabetes by BMI")
    + xlab("BMI")
    + ylab("Number of People")
    + theme(
        plot_title=element_text(size=PLOT_TITLE_SIZE),
        axis_title=element_text(size=AXIS_TITLE_SIZE),
        axis_text_x=element_text(rotation=0, hjust=0.3), 
        legend_position = (.765, .77), 
        legend_title=element_blank()
        )
    )
    return save_graph(graph, "bmi_graph") 


generate_graphs()