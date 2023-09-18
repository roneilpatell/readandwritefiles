import csv 

employee = open('EmployeePay.csv', 'r')


csv_file = csv.reader(employee)

next(csv_file)

for record in csv_file:
    print(f'First Name: {record[1]}')
    print(f'Last Name: {record[2]}')
    salary = float(record[3])
    print(f'Salary:\t $ {salary:10,.2f}')
    bonus = float(record[4])
    totalBonus = salary * bonus
    print(f'Bonus:\t $ {totalBonus:10,.2f}')
    totalPay = salary + totalBonus
    print(f'Pay:\t ${totalPay:10,.2f}')
    input()


