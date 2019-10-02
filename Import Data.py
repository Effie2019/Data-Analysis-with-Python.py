# import pandas library
import pandas as pd
# Read the online file by the URL provides above, and assign it to variable "df", no header
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)

# show the first 5 rows using dataframe.head() method
df.head(5)
# Add headers 
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
#drop missing value
df.dropna(subset=["price"], axis=0)
#data types
df.dtypes()
#get a statistical summary of each column
# including object-typed attributes
df.describe()
df.describe(include="all")
