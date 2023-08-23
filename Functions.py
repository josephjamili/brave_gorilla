# Here, we're createing two functions to use our frequency table:

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

def freq_table(column):
    frequency_table = {}
    for value in column:
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
    return frequency_table

genres_ft = freq_table(genres)
print(genres_ft)

# Below, we're working on writing a single function, rather that two, to create frequency tables.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = {}
def freq_table(column):
    for row in apps_data[1:]:
        column = row[7]
        if column in ratings:
            ratings[column] += 1
        else:
            ratings[column] = 1
    return ratings

ratings_ft = freq_table(apps_data)
print(ratings_ft)

# Working with reusability of functions. Here the function should take in two inputs: a dataset and the index of
# a column (name the columns whatever your want). Inside the function's body: 1) loop through the date set using
# that parameter, which will be a dataset (a list of lists). For each iteration, select the value you want by using
# the parameter, which will be an index number. 2) Build the frequency table as a dictionary
# The function should retunrn the frequency table as a dictionary

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table
ratings_ft = freq_table(data_set=apps_data, index=7)
print(ratings_ft)

