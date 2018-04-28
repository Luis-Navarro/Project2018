# Project2018
This repository includes material for the Project.

Pyhon 3.6. For running the code it is recommended to download and install anaconda.
Libraries used: pandas, scipy, numpy
script: [iris_analysis.py](https://github.com/Luis-Navarro/Project2018/blob/master/iris_analysis.py)


## 1. Research and description
As one of the most famous datasets used in several disciplines, the first step is to research on the existing literature to obtain an accurate approach to this particular dataset's characteristics and previous researches carried out.

The dataset, in comma separated value (CSV) format can be downloaded from [UCI Machine Learning website](http://archive.ics.uci.edu/ml/datasets/Iris?ref=datanews.io).

### Definition
This dataset consists in four measurements in centimeters for the variables sepal length and width, and petal length and width, for 150 flowers representing three species of iris (Iris setosa, versicolor and virginica). The Iris Flower Dataset is a popular multivariate dataset that was introduced by R.A. Fisher as an example for discriminant analysis.

### Methodological Approach
The first approach to the iris data set was, obviously, following the exercises and using the resources seen during the course. However, after some very basics displays, it soon was revealed that a more complex approach could be adopted. After researching and testing different features from the numpy library, almost all online references consulted pointed towards a combination of three basic libraries: the aforementioned numpy, the scientific library scipy (which includes matplotlib, the basic library for plotting, among other interesting features) and pandas. This latter library offers the possibility of structuring data for its analysis.
Several days were spent researching and testing these libraries, and the first attempts to manipulate data, looping through the dataset and slicing different columns, were soon replaced for more complex, accurate and time-saving approaches.

The first attempt to structure the data set was tested with the genfromtext attribute included in the numpy library. Some testing can still be found on [this first version](https://github.com/Luis-Navarro/Project2018/blob/master/iris%20analysis_pandas.py). However, the problems found when trying to include the variables' names at the top of each column took this script to a dead-end road. Several days were spent resarching online until this was solved. The workaround consisted in specifying the strings using 'names'within np.genfromtext function.

During the online research some examples found were avoiding this problem by transforming data into a data frame, which, after some more investigation, resulted in the most appropriate way to deal with the data for analysing and plotting data. Furthermore, when replacing numpy.genfromtext for a more specific pandas.read_csv order, data obtained a more structural format, which allowed to get rid of extra scripting, as the column name specification commented above.

However, numpy includes describe, a very useful function that saved a lot of time of coding and slicing columns, resulting in a very neat table showing the main descriptive calculations for numeric variables. Count, average, max, min and quartile description is specified for each column. 

Therefore, pandas and numpy combined together provide the dataset with a structured and statistically functional format. From here on, matplotlib was used to illustrate the main statistical findings unveiled by the accuracy of numpy and pandas, in an attempt to provide the script with a logical sequence, going from reading the data, structure it, showing the basic descriptive results, transforming data into a date frame and, finally, using multivariable analysis to discover relations among variables.

This project's development has been gradual, incorporating new features as they were found useful during the research. Every new feature introduced opened new development opportunities. In fact, the multiple possible development areas had to be registered in order to optimize and decide which of them, and in which order, werre worth to research, test and include in the code. Obviously, some of those had no room in this script, but they point to possible future scenarios. A track of these research lines can be found [here](https://github.com/Luis-Navarro/Project2018/blob/master/improvements.txt)

### Bibliography
See [resources](https://github.com/Luis-Navarro/Project2018/blob/master/resources.txt)

## 2. Analysis
As explained above, this project was designed to tackle iris data set investigation from basic to complex, from describing variables to attempt to provide some explanation about the relations among them. Therefore, analysis was divided in two stages: description and multivariable interaction.

### Descriptive analysis

- measures of central tendency (mean, median, mode)
- plotting 

### Multivariable analysis

- 



