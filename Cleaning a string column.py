import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)

# While it appears that the weight column may just need the kg characters removed from the end of each string, 
# there is one special case - one of the values ends with kgs, so you'll have to remove both kg and kgs characters.

# Steps:
# Convert the values in the weight column to numeric values.
# Rename the weight column to weight_kg.
# Use the DataFrame.to_csv() method to save the laptops dataframe to a CSV file laptops_cleaned.csv without index labels.

laptops["weight"] = laptops["weight"].str.replace("kg","").str.replace("kgs","").str.replace("s","").astype(float)
laptops.rename({"weight":"weight_kg"}, axis=1, inplace=True)
laptops.to_csv("laptops_cleaned.csv", index=False)