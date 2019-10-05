#PREP
#Print the dimensions of the dataframe
print(df_can.shape)
#Rename the columns name
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
#Set one column as index
df_can.set_index('Country', inplace=True)
#Add a total column
df_can['Total'] = df_can.sum(axis=1)
#Sort Value
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
