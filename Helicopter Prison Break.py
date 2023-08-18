#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# In this project, we will attempt to answer the following questions:
# - In which year did the most helicopter prison break attempts occur?
# - In which countries do the most attempted helicopter prison escapes occur?

# We begin by importing some helper functions.

# In[30]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes]
# (https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[31]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)


# Let's print the first three rows

# In[32]:


for row in data:
    index = 0
    data[index] = row[:-1]
    index += 1

print(data[:3])


# We using fetch_year() function to extract the year. Inside the loop, we're replacing the first element of the current row (i.e. row[0]) with the result obtained from the fetch_year() function. Which takes the first element of the row as its input.

# In[33]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date

print(data[:3])


# In[34]:


#code for the earliest and latest years in the data:

min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# Let's check the max and min year

# In[35]:


print(min_year)
print(max_year)


# In[36]:


#code used to generate a list of all the years betwen min_year and max_year:

years = []
for year in range(min_year, max_year + 1):
    years.append(year)

#print the years to inspect the max and min
print(years)


# In[37]:


attempts_per_year = [] #creating the list

for year in years:
    attempts_per_year.append([year, 0])

print(attempts_per_year)


# We will be doing some nested loops. We start by iterating over our starting data (stored in the variable data)

# In[42]:


for row in data:# Instruction 1 - for each row in data
    for year_attempt in attempts_per_year: # Instruction 2 - nothing to do here
        # Instruction 3 - assign the year value in year_attempt to year
        year = year_attempt[0]
        if row[0] == year:
            year_attempt[1] += 1

# Instruction 4 - print the results
print(attempts_per_year)


# ## We can visualize and answer to the question, "In which year did the most attempts at breaking out of prision with a helicopter occur?" by using information from the code generated previously.

# In[43]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# Based on the information provided from the bar graph, the years in which helicopter escapes occured more frequently between 1973 - 2020 are 1986, 2001, 2007, and 2009, and 2020.

# ## We are going to answer another question in this project, "In which countries do the most attempted helicopter prison excapes occur?". The code below counts the number of helicopter escapes for each country.

# In[44]:


countries_frequency = df["Country"].value_counts()

print_pretty_table(countries_frequency)


# From this table, we see that France is the country with the most helicopter prison escape attempts.
