import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

# isloating rows with values of 20% or more

slowness_20_or_more = traffic[traffic['Slowness in traffic (%)'] >= 20] # isloating rows with values of 20% or more
slowness_20_or_more = slowness_20_or_more.drop(['Slowness in traffic (%)',
                                                'Hour (Coded)'], axis=1)
# droping the columns

# using pandas to calculate an event series, then using this series to plot a horizontal bar graph
incident_frequencies = slowness_20_or_more.sum()
incident_frequencies.plot.barh()
plt.show()