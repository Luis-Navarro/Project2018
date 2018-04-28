# Luis Navarro. Project 2018. 
# April 2018 Iris Data Set analysis
# This script was made adapting several publicly  published code from several sources online. 
# Please check the file resources.txt for a complete relation of resoures used and code adapted.

# importing libraries 
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Reading dataset with Pandas
data = pd.read_csv("data/iris.csv")

# Summary
print (data["variety"].value_counts())
data.plot(kind="scatter", x="sepal.length", y="sepal.width") # plots Sepal
data.plot(kind="scatter", x="petal.length", y="petal.width") # plots Petal
plt.show() # displaying plots

# Descriptive Analysis 
df = pd.DataFrame(data) # Creating data frame
print (df.describe()) # Descriptive statistics. Average, Max, Min, Std deviation, etc.

df.boxplot() # plots boxes. Explores disperssion from average
df.hist() # plots histograms
plt.show() # displaying plots

# Multivariable analysis
print (df.corr()) #Correlation matrix
scatter_matrix(df) # plots scatter - disperssion. Explores correlations
plt.show() # displaying plots

