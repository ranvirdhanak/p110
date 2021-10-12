import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv

df = pd.read_csv('kaggle2.html')
data = df['population'].tolist()

dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
stdev = statistics.stdev(dataset)
print(mean)
print(stdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
         random_index = random.randint(0,len(data))
         value = data[random_index]
         dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],['temp'],show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()
population_mean = statistics.mean(data)
print("population mean = ",population_mean)
stev = statistics.stdev(data)
print("stdev = ",stev)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    stdev2 =  statistics.stdev2(mean_list)
    print("stdev2_of_sampling_distribution = ",stdev2)
standard_deviation()


