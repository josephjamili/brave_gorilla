# Summarizing Artwork Gender Data with Frequency tables

gender_freq = {}
for row in moma:
    gender = row[5]
    if gender not in gender_freq:
        gender_freq[gender] = 1
    else:
        gender_freq[gender] += 1

for gender, num in gender_freq.items():
    template = "There are {n:,} artworks by {g} artists"
    output = template.format(g=gender, n=num)
    print(output)
        