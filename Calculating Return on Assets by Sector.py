import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)


# The column we create is going to contain a metric called return on assets (ROA). 
# ROA is a business-specific metric which indicates a company's ability to make profit using their available asset.

# Once we've created the new column, we'll aggregate by sector, and find the company
# with the highest ROA from each sector

# Create a new column roa in the f500 dataframe, containing the return on assets metric for each company
f500["roa"] = f500["profits"] / f500["assets"]
roa = f500["roa"]


# Aggregate the data by the sector column, and create a dictionary top_roa_by_sector, with:
# 	Dictionary keys with the sector name.
# 	Dictionary values with the company name with the highest ROA value from that sector.

top_roa_by_sector = {}

sector = f500["sector"].unique()

for s in sector:
    selected_rows = f500[f500["sector"] == s]
    sorted_rows = selected_rows.sort_values("roa", ascending=False)
    top_roa_by_sector[s] = sorted_rows.iloc[0]["company"]