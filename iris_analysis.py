# Luis Navarro. Project 2018. April 2018 Iris Data Set analysis

# importing libraries 
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Reading dataset with Pandas
data = pd.read_csv("data/iris.csv")

# Summary
print (data["variety"].value_counts())


# Descriptive Analysis 
df = pd.DataFrame(data)
print (df.describe())
data.plot(kind="scatter", x="sepal.length", y="sepal.width")
data.plot(kind="scatter", x="petal.length", y="petal.width")

df.boxplot()
df.hist()
plt.show()

# Multivariable analysis
df.corr()
scatter_matrix(df)
plt.show()

