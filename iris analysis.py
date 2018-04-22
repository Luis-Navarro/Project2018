# Luis Navarro. Project 2018. April 2018
# Iris Data Set analysis

# importing libraries 
import pandas as pd
import numpy as np

# Printing dataset
with open ("data/iris.csv") as iris:
  for line in iris:
    line = line.replace(',', ' ')
    line = line.rstrip()
    print(line)

# Loading dataset with numpy
data = np.genfromtxt ("data/iris.csv", delimiter=",")
firstcol = data[:,0]
meanfirstcol = np.mean (data[:,0])
print ("The mean values for the first column is ",meanfirstcol)

seccol = data[:,1]
meanseccol = np.mean (data[:,1])
print ("The mean values for the second column is ",meanseccol)
