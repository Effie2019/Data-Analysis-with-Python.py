#0.LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
#1.IMPORT DATA
# Read the online file by the URL provides above, and assign it to variable "df", no header
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)
# Add headers 
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
# Give hearders, then read file
df = pd.read_csv(other_path, header=headers)
# Show the first 5 rows using dataframe.head() method
df.head(5)
# a.Get the type of each column of the datafrome
# b.Get a statistical summary of each column
# c.Including object-typed attributes
# d.look at the info of "df"
df.dtypes()
df.describe()
df.describe(include="all")
df.describe(include=['object']) #Apply the method "describe" on the variables of type object
df.info
#Drop missing value
df.dropna(subset=["price"], axis=0)

#2.DATA WRANGLING
#Missing Value
#a.Dentify missing data
missing_data = df.notnull()
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())#Count the value in each category
    print("")    
#b.Deal with missing data
df.replace("?", np.nan, inplace = True) #replace ? by nan
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0) #Calculate the mean of the "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True) #Replace "NaN" by mean value in "normalized-losses" column
#c.Correct data format
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")

#BINNING DATA
#1.Convert the data to correct format
df["horsepower"]=df["horsepower"].astype(int, copy=True)
#2.Histogram
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"])#plt.pyplot.hist(df["horsepower"], bins = 3)
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
#3.Cut
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df["horsepower-binned"].value_counts()#See the counts in each bin

#LINEAR RELATIONSHIP
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)#the start point of y is 0
sns.boxplot(x="body-style", y="price", data=df)

