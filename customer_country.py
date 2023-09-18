import csv

customers = open('customers.csv', 'r')
newCustomers = open('customer_country.csv', 'w')

csv_file = csv.reader(customers)

next(csv_file)

count = 0

for record in csv_file:
    newCustomers.write(f'{record[1]} {record[2]}, {record[4]}' '\n')
    count+=1

print("Total records:", count)
    