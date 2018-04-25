# Luis Navarro. Project 2018. April 2018 Iris Data Set analysis

# importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Loading dataset with numpy
data = np.genfromtxt ("data/iris.csv", delimiter=",", names = ["seplen", "sepwid", "petlen", "petwid", "species"])

#using pandas to transform data into dataframe
df = pd.DataFrame(data, columns = ["seplen", "sepwid", "petlen", "petwid", "species"], dtype=float)

# Size of the Data Frame
print (df.shape)

# Descriptive Analysis 
print (df.describe())


df.hist()
plt.show()