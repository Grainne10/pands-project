# analysis.py
# This project is for the programme and scripting module in the Higher Diploma in Science in Data Analytics
# It is based on the Fisher's Iris Data Set
# Author Grainne Boyle

# The first step is to import pandas . Pandas is an open source library used for data analysis and manipulation of data frames/datasets. 

import pandas as pd
 
# Next I load the Iris data set into a data frame using df in pandas
# A DataFrame is a 2 dimensional data structure, like a 2 dimensional array,or a table with rows and columns.
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

#I do some review of the data
# It gives you a brief overview of the data by columns, count, types
print(df.info())
# Brief description of the count, mean, std dev, min
print(df.describe())
# This will show if there are missing data or if the dataset is complete.  "True" shows that the value is missing in that field.
# There are no missing values.  This is an example of a Boolean.  
print(df.isnull())
print(df.isnull().sum())
# This will show you the type of data that you are analysing. It determines Sepal length, Sepal Width,  Petal Length and Petal Width as the numbers are fractitional it detects they are floating numbers.  
# Species are shown as objects. Typically, objects means that the values in the columns are strings or a mixture of data types. 
print(df.dtypes)


# To show the headers, it will show the first and last five
print(df.head())


# If we want   see the number of each Species column, we can use this formula.
# We can see we have 3 unique species. All species contains equal amounts or rows.
df["species"].value_counts() 


# Output a summary of the each variables to a single text file.

from io import StringIO

# Capture the output of df.info() into a string - for this String IO section, I could not find why the info section would not print to the file
# So I looked it up on chat GPT and it suggested using this. I did further research and added it to the readme file. 
# Without this it was printing to code rather than returning a value to the file. 
#StringIO allows you to treat strings like file-like objects and captures the output of your dataframe info as a string
buffer = StringIO()
df.info(buf=buffer)
info_output = buffer.getvalue()
buffer.close()

# This section I created myself .

with open(r"iris_summary.txt", "w") as f:

    describe = str(df.describe())
    info = str(df.info()) 
    null = str(df.isnull().sum)
    summary =  info_output + "\n\n" + describe + "\n\n" + null

    # Write the summary to the file
    f.write(summary)



# The data set is clean, has no missing values and is ready for analysis.


# We will look at how some of these individual variables look different charts and plots.
# In order to do this, we must import matplotlib, it is a library for creating visualisations in python. It is generally used for basic chart plotting.

 
import matplotlib.pyplot as plt



# We will install Numpy. NumPy is a python library, it can be used to perform advanced mathematical tasks quickly.

import numpy as np


# Seaborn can be imported and used by matplotlib to draw its plots.  
# Seaborn is another python data visualisation library based on matplotlib, it integrates with pandas data structures. 
# It provides aesthetic data visualisations.
import seaborn as sns

#To ignore warnings, re: the figure layout changes, we import the warnings module
import warnings
warnings.filterwarnings('ignore')

# Scatter plots use dots to represent values for two different numeric variables.
# Scatter plots are used to observe relationships between variables.
# This is a scatterplot of the sepal length vs sepal width and I show the plots in different shapes to identify them clearly
sns.scatterplot(df, x="sepal_length", y="sepal_width", hue="species", style="species", markers={"setosa": "^", "versicolor": "s", "virginica": "o"})
plt.title("Scatter Plot of Sepal Length vs. Sepal Width")
plt.xlabel("Sepal Length (Cm) ")
plt.ylabel("Sepal Width (Cm) ")
plt.legend(loc='upper right', bbox_to_anchor=(1.30, 1))
plt.savefig('Scatter plot of Sepal Length vs Sepal Width ', bbox_inches='tight')
plt.show()

# This is a scatterplot of the petal length vs petal width and I show the plots in different shapes to identify them clearly.
sns.scatterplot(df, x="petal_length", y="petal_width", hue="species", style="species", markers={"setosa": "^", "versicolor": "s", "virginica": "o"})
plt.title("Scatter Plot of Petal Length vs. Petal Width")
plt.xlabel("Petal Length (Cm) ")
plt.ylabel("Petal Width (Cm) ")
plt.legend(loc='upper right', bbox_to_anchor=(1.30, 1)) 
plt.savefig('Scatter plot of Petal Length vs Petal Width ', bbox_inches='tight')
plt.show()

# A pairplot combines both histogram and scatter plots, it provides an overview of each pair of variables and shows the dataset's distributions and correlations. If the variables tend to increase and decrease together, the association is positive.
# This is a pairplot using seaborn. This shows the scatter plots and kernal density plots for all variables
sns.pairplot(df, hue="species", markers=["o", "s", "^"])
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.savefig('Pairplot of Iris Dataset', bbox_inches='tight')
plt.show()



# Facet grids maps the dataset onto multiple axes.
# It visualises the distribution of variables of the dataset and the relationship between variables. 
# I use it to show each of the species separately and clearly. T
# This facet grid shows a scatterplot of sepal length vs sepal width

g = sns.FacetGrid(df, col="species",  hue="species", height=5, aspect=1.2)
g.map(sns.scatterplot, "sepal_length", "sepal_width")
g.set_axis_labels("Sepal Length (cm)", "Sepal Width (cm)")
g.set_titles("{col_name}")
plt.subplots_adjust(top=0.85) 
plt.suptitle("Facet Grid Sepal Length  vs. Sepal Width ", fontsize=18)
plt.savefig('Facet Grid Scatter plot of Sepal Length vs Sepal Width of Iris Species', bbox_inches='tight')
plt.show()

# This facet grid shows a scatterplot of petal length vs petal width
g = sns.FacetGrid(df, col="species",  hue="species", height=5, aspect=1.2)
g.map(sns.scatterplot, "petal_length", "petal_width")
g.set_axis_labels("Petal Length (cm)", "Petal Width (cm)")
g.set_titles("{col_name}")
plt.subplots_adjust(top=0.85) 
plt.suptitle("Facet Grid Petal Length  vs. Petal Width ", fontsize=18)
plt.savefig('Facet Grid Scatter plot of Petal Length vs Petal Width of Iris Species', bbox_inches='tight')
plt.show()


# A boxplot demonstrates graphically the locality, spread and skewness of groups of numerical data through their quartiles.
# The spacings in the subsections of the box-plot indicate the degree of spread and skewness of the data.
# It also displays outliers that differ from the rest of the dataset.
# I show a boxplot of the four variables in the dataset.
plt.figure(figsize=(10, 8))
sns.boxplot(data=df, orient="v", palette="Set2")
plt.ylabel('Measurement (cm)')
plt.title('Box Plot of Iris Dataset')
plt.savefig('Box Plot of Iris Dataset')
plt.show()


# Histograms are visual representation of the distribution of quantitative data.It takes all the data and divides the entire range of values into a series of intervals.
# it counts how many values fall into each interval. 
# This is a histogram of sepal length
plt.figure(figsize=(6, 6))
sns.histplot(df, x='sepal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
plt.title('Histogram Sepal Length')
plt.legend
plt.xlabel('Sepal Length')
plt.ylabel('Count')
plt.xticks(rotation=45) 
plt.savefig('Histogram Sepal Length')
plt.show()

# This is a histogram of sepal width
plt.figure(figsize=(6, 6))
sns.histplot(df, x='sepal_width', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=16, alpha=0.3)
plt.title('Histogram Sepal Width')
plt.legend
plt.xlabel('Sepal Width')
plt.ylabel('Count')
plt.savefig('Histogram Sepal Width')
plt.show()

# This is a histogram of petal length
plt.figure(figsize=(6, 6))
sns.histplot(df, x='petal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
plt.title('Histogram Petal Length')
plt.legend
plt.xlabel('Petal Length')
plt.ylabel('Count')
plt.savefig('Histogram Petal Length')
plt.show()

# Thi is a histogram of petal width
plt.figure(figsize=(6, 6))
sns.histplot(df, x='petal_length', hue="species", edgecolor = "white", multiple="layer", kde=True, bins=18, alpha=0.3)
plt.title('Histogram Petal Width')
plt.legend
plt.xlabel('Petal Width')
plt.ylabel('Count')
plt.savefig('Histogram Petal Width')
plt.show()

# To show correlation coefficient for numeric values we can use do a matrix. Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Print correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# We can use the correlation matrix to plot a heatmap
# Heatmaps use a colour coding system to represent different values. They allow you to quickly identify patterns and anomalies.
# We can use annot to show the values and fmt for decimal places
# This shows a heatmap of all the variables
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5) 
plt.title('Correlation Heatmap of Iris Dataset Variables')
plt.savefig('Iris DataSet HeatMap')
plt.show()

# A violin plot is a hybrid of a box plot and a kernel density plot, which shows peaks in the data. 
#It is used to visualize the distribution of numerical data. 
# This is a violin plot for each variable in the Iris Data Set
 
fig, axes = plt.subplots(2, 2, figsize=(18, 10))
 
fig.suptitle('Iris Data Set Violin Plots')
 
 
sns.violinplot(df, x='species', y='sepal_length', ax=axes[0, 0] )
sns.violinplot(df, x='species', y='sepal_width', ax=axes[0, 1] )
sns.violinplot(df, x='species', y='petal_length', ax=axes[1, 0] )
sns.violinplot(df, x='species', y='petal_width', ax=axes[1, 1])
plt.savefig('Iris DataSet Violin Plots')
plt.show()

# Andrews Curves can be used as a way to visualise multivariate data. It maps all features from a row of data onto a function resulting in a unique curve. It highlights potential clusters or separations from them.
# This is an Andrew's curves plot :

plt.figure(figsize=(10, 8))
pd.plotting.andrews_curves(df, 'species', colormap='plasma')
plt.title('Iris Dataset Andrews Curves')
plt.legend(loc='upper right')
plt.savefig('Iris DataSet Andrews Curves')
plt.show()

# Extract data
#data = df.iloc[:, :-1]  # Selecting all rows and all columns except the last one
#feature_names = df.columns[:-1]  # Extracting feature names from DataFrame columns

# To save a table into a png file so it can be copied into the Readme file.

from pandas.plotting import table

df = pd.DataFrame()
df['sepal_length'] = ['150.000000', '5.843333', '0.828066', '4.300000', '5.100000', '5.800000', '6.400000', '7.900000']
df['sepal_width'] = ['150.000000', '3.057333', '0.435866', '2.000000', '2.800000', '3.000000', '3.300000', '4.400000']
df['petal_length'] = ['150.000000', '3.758000', '1.765298', '1.000000', '1.600000', '4.350000', '5.100000', '6.900000']
df['petal_width'] = ['150.000000', '1.199333', '0.762238', '0.100000', '0.300000', '1.300000', '1.800000', '2.500000']

index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
df.index = index

plt.figure(figsize=(7, 2))
ax = plt.subplot(111, frame_on=True)  
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
table(ax, df, loc="center")  # where df is your data frame

plt.savefig("describetable.png")

# Add in a missing values table similar to one above
null_counts = {'sepal_length': 0, 'sepal_width': 0, 'petal_length': 0, 'petal_width': 0, 'species':0}
df_null_counts = pd.DataFrame(null_counts.items(), columns=['Column', 'Missing Values'])

# Plotting the table and saving it as an image file
plt.figure(figsize=(4, 3))  # Adjust the figure size as needed
ax = plt.subplot(111, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

table(ax, df_null_counts, loc='center')
plt.savefig("Missing values Table.png")

