# Luis Navarro. Project 2018. April 2018 Iris Data Set analysis

# importing libraries 
import pandas as pd
import numpy as np

# Loading dataset with numpy
data = np.genfromtxt ("data/iris.csv", delimiter=",", names = ["seplen", "sepwid", "petlen", "petwid", "species"])

#separating data into columns
d = {'seplen': data[:,0], 'sepwid': data[:,1], 'petlen': data[:,2], 'petwid': data[:,3]}

#using pandas to transform data into dataframe
df = pd.DataFrame(data=d)

# Size of the Data Frame
print (df.shape)

# Descriptive Analysis 
print (df.describe(include=[np.number]))

# Including flower species in the Data Frame
d = {'seplen': data[:,0], 'sepwid': data[:,1], 'petlen': data[:,2], 'petwid': data[:,3], 'species': data [:,4]}
print (df.describe())


byspecies = data.groupby('species')