import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
traffic_per_day = {}
for i, day in zip(range(0, 135, 27), days):
    each_day_traffic = traffic[i:i+27]
    traffic_per_day[day] = each_day_traffic

plt.figure(figsize=(10,12))

for i, day in zip(range(1, 6), days):
    plt.subplot(3, 2, i)
    plt.plot(traffic_per_day[day]['Hour (Coded)'],
            traffic_per_day[day]['Slowness in traffic (%)'])
    plt.ylim([0,25])
    plt.title(day)

plt.show()