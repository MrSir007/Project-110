import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics
import random

getData = pd.read_csv("medium_data.csv")
datalist = getData["reading_time"].tolist()

meanData = statistics.mean(datalist)
devData = statistics.stdev(datalist)

def findMean (counter) :
  sample = []
  for i in range (0,counter) :
    index = random.randint(0,len(datalist))
    value = datalist[index]
    sample.append(value)
  meanSample = statistics.mean(sample)
  devSample = statistics.stdev(sample)
  return meanSample

def graph (meanlist) :
  data = meanlist
  distribution = pff.create_distplot([data],["Reading Time"],show_hist=False)
  distribution.show()

def setup () :
  meanlist = []
  for i in range (0,1000) :
    meanSample = findMean(100)
    meanlist.append(meanSample)
  graph(meanlist)

setup()