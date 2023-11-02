# 
import matplotlib.pyplot as plt
import pandas as pd

class dataLoader:
    def __init__(self,source):
        self.source=source

    def load_data(self):
        data=pd.read_csv(self.source)
        return data
    
class DataProcessor:
    def __init__(self,data):
        self.data=data

    def cleanData(self):
        cleaned_data=self.data.dropna()
        return cleaned_data
    
    def transformData(self):
        return self.data
    
class dataVisulization:
    def __init__(self,processed_data):
        self.data=processed_data

    def plot_graph1(self,feature):
        plt.xlabel(feature)
        plt.ylabel('frequency')
        plt.title('graph1 of {feature}')
        plt.show()

    def plot_graph2(self,xfeature,yfeature):
        plt.xlabel(xfeature)
        plt.ylabel(yfeature)
        plt.title('graph2 of {feature}')
        plt.show()

    def plot_graph1(self,xfeature,yfeature):
        plt.xlabel(xfeature)
        plt.ylabel(yfeature)
        plt.title('graph2 of {feature}')
        plt.show()
        
data_loader = dataLoader("data.csv")
raw_data = data_loader.load_data()

data_processor = DataProcessor(raw_data)
processed_data = data_processor.clean_data()
processed_data = data_processor.transform_data()

data_visualizer = dataVisulization(processed_data)
data_visualizer.plot_histogram("age")
data_visualizer.plot_scatter("income", "spending")
data_visualizer.plot_bar_chart("category", "count")

        


        