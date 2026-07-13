import csv

file = open('finacialyear.csv', 'r')
data = csv.reader(file)

print("Printing the data from csv file")
for row in data:
    print(row)
file.close()


# filter 1

file = open('finacialyear.csv', 'r')
data = csv.reader(file)

print("Printing the data from csv file for year 2022")
for row in data:
    if row[0] == '2022':
        print(row)
file.close()

# filter 2

file = open('finacialyear.csv', 'r')
data = csv.reader(file)

print("Printing the data from csv file for industry of agriculture sector")
for row in data:
    if row[2] == 'Agriculture, Forestry and Fishing':
        print(row)
file.close()

# filter 3

file = open('finacialyear.csv', 'r')
data = csv.reader(file)

print("Printing the data from csv file for industry of agriculture but only for total income from variable cost")
for row in data:
    if row[2] == 'Agriculture, Forestry and Fishing' and row[4] == 'Total income':
        print(row)
file.close()

# filter 4

file = open('finacialyear.csv', 'r')
data = csv.reader(file)

print("Printing the data from csv file for index code only p and  H")
for row in data:
    if row[1] == 'P' or row[1] == 'H':
        print(row)
file.close()