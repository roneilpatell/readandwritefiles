import csv 


sales = open('sales.csv', 'r')
salesReport = open('sales_report.csv', 'w')

csv_file = csv.reader(sales)

next(csv_file)

custId= 'Customer ID'
total = 0
for record in csv_file: 
    if (record[0] == custId):
        total += float(record[3]) + float(record[4]) + float(record[5])
    else:
        salesReport.write(f'{custId}, {total:.2f}\n')
        custId = record[0]
        total = float(record[3]) + float(record[4]) + float(record[5])

salesReport.write(f'{custId}, {total:.2f}\n')


