# Next, you'll use the array method for finding the mean values of specific columns 
# in our cleaned data. Here are the columns we're interested in:
# trip_distance = column index 7
# trip_length = column index 8
# total_amount = column index 13
# Next, you'll use the array method for finding the mean values of specific columns in our cleaned data. Here are the columns we're interested in:

#Use trip_mph to create a new ndarray, cleaned_taxi, containing only rows for which the values of trip_mph are less than 100.
# 1. Calculate the mean of the trip_distance column of cleaned_taxi. Assign the result to mean_distance.
# 2. Calculate the mean of the trip_length column of cleaned_taxi. Assign the result to mean_length.
# 3. Calculate the mean of the total_amount column of cleaned_taxi. Assign the result to mean_total_amount.

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')

trip_distance = taxi[:, 7] # trip distance in miles
trip_length = taxi[:, 8] / 3600 # trip length in hours
trip_mph = trip_distance / trip_length # average trip speed in mph

cleaned_taxi = taxi[trip_mph < 100]

mean_distance = cleaned_taxi[:, 7].mean()
mean_length = cleaned_taxi[:, 8].mean()
mean_total_amount = cleaned_taxi[:, 13].mean()