# Python program to convert JSON file to CSV. Source code is primarily from https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
import json
import csv

# If a required field is not in input json, set it to blank
# Remove leading and trailing spaces
def format_fields(record, fieldnames):
	for field in fieldnames:
		if field not in record:
			record[field] = ''
		if record[field] != None:
			record[field] = record[field].strip()

# Opening JSON file and loading the data into the variable data
filename_json = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_grievance.json'
filename_csv = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_grievance.csv'

with open(filename_json, encoding='utf8') as json_file:
	data = json.load(json_file)

grievance_data = data

# now we will open a file for writing
data_file = open(filename_csv, 'w', encoding='utf8', newline='')

# create the csv writer object
#csv_writer = csv.writer(data_file)
fieldnames = ['registration_no', 'org_code', 'dist_name', 'pincode', 'state', 'sex']
csv_writer = csv.DictWriter(data_file, fieldnames=fieldnames)

# Counter variable used for writing 
# headers to the CSV file
count = 0

for record in grievance_data:
	if count == 0:
		count += 1
		csv_writer.writeheader()

    # Writing data of CSV file
	format_fields(record, fieldnames)
    #TODO - Below hard coding of field names can be optimized further
	csv_writer.writerow({'registration_no': record['registration_no'], 'org_code': record['org_code'], 'dist_name': record['dist_name'], 
					  'pincode': record['pincode'], 'state': record['state'], 'sex': record['sex']})

data_file.close()



