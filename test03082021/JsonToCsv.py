import json
import csv
from datetime import datetime

# Opening JSON file and loading the data
# into the variable data
with open('data.json') as json_file:
    data = json.load(json_file)


class write_to_csv:
    def generate_csv(data):
        employee_data = data['emp_details']
        filename = 'data_' + str(datetime.now().strftime("%H_%M_%S")) + '.csv'
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


