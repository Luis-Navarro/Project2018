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

The first attempt to structure the data set was tested with the genfromtext attribute included in the numpy library. Some testing can still be found on [this first version](https://github.com/Luis-Navarro/Project2018/blob/master/iris%20analysis_pandas.py). However, the problems found when trying to include the variables' names at the top of each clomun took this script to a dead-end road. Several days were spent resarching online until this was solved. The workaround consisted in specifying the strings using 'names'within np.genfromtext function.



### Bibliography
See [resources](https://github.com/Luis-Navarro/Project2018/blob/master/resources.txt)

## 2. Analysis

### Descriptive analysis

- measures of central tendency (mean, median, mode)
- plotting 

### Multivariable analysis

- 



