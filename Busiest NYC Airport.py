import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')

# Let's determine the busiest airport by 
# checking the pickup_location_code column (column index 5) for these specific values:
# 2 = JFK Airport
# 3 = LaGuardia Airport
# 5 = Newark Airport

jfk = taxi[taxi[:, 5] == 2]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:, 5] ==3]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:, 5] == 5]
newark_count = newark.shape[0]

busiest_airport = "laguardia"