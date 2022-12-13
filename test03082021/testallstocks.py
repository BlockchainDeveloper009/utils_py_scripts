
import json
import csv
from datetime import datetime
file0= 'aapl_historical_stock_prices.json'
p0='AAPL'
file1 = 'aapl_history.json'
p1 = 'prices'
# Opening JSON file and loading the data
# into the variable data
with open(file1) as json_file:
    data = json.load(json_file)

    employee_data = data[p1]
    filename = file1 + str(datetime.now().strftime("%H_%M_%S")) + '.csv'
    # now we will open a file for writing
    data_file = open(filename, 'w')

     # create the csv writer object
    csv_writer = csv.writer(data_file)

     # Counter variable used for writing
     # headers to the CSV file
    count = 0

    for emp in employee_data:

        if count == 0:
            # Writing headers of CSV file
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1

            # Writing data of CSV file
            csv_writer.writerow(emp.values())

data_file.close()