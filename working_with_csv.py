from pathlib import Path
import csv

# Writing to a csv file
try:
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['no', 'name', 'count'])
        writer.writerow([1, 'one', 3])
        writer.writerow([2, 'two', 7])
except Exception as e:
    print(e)

# Reading from a csv file
try:
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except Exception as e:
    print(e)
