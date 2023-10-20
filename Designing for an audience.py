import pandas as pd
import matplotlib.pyplot as plt

top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

fig, ax = plt.subplots(figsize=(4.5, 6))
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#af0b1e')
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)
ax.set_xticks([0, 150000, 300000])
ax.set_xticklabels(['0', '150,000', '300,000'])
ax.xaxis.tick_top()
ax.tick_params(top=False, left=False)
ax.tick_params(axis='x', colors='grey')
ax.text(x=-80000, y=23.5,
        s='The Death Toll Worldwide Is 1.5M+',
        weight='bold', size=17)
ax.text(x=-80000, y=22.5,
        s='Top 20 countries by death toll (December 2020)',
        size=12)

ax.set_yticklabels([]) # an empty list removes the labels
country_names = top20_deathtoll['Country_Other']

# using zip function to left-align by applying a for loop over country names
for i, country in zip(range(0,20), country_names): 
    ax.text(x=-80000, y=i-0.15, s=country)
ax.axvline(x=150000,ymin=0.045, c='grey', alpha=0.5) # altering the appearance of the vertical line

plt.show()