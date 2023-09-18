import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers)

next(csv_file)


for record in csv_file:
    print(record)
    print(f'First Name: {record[1]}')
    print(f'Last Name: {record[2]}')
    input()