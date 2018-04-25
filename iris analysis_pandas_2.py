# Luis Navarro. Project 2018. April 2018 Iris Data Set analysis

# importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading dataset with Pandas
data = pd.read_csv("data/iris.csv")

# Summary
print (data["variety"].value_counts())

data.plot(kind="scatter", x="sepal.length", y="sepal.width")
data.plot(kind="scatter", x="petal.length", y="petal.width")
# Descriptive Analysis 
df = pd.DataFrame(data)
print (df.describe())

df.hist()
plt.show()

