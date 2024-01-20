# Python program to convert JSON file to CSV. Source code is primarily from https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
import json
import csv

# Initialise file names used in this script
report_json_file_name = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_grievance_small.json'
history_json_file_name = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_action_history_small.json'
history_json_file_temp_name = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_action_history_temp.json'
gievance_merged_csv_file_name = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\grievance_merged_history.csv'

# If a required field is not in input json, set it to blank
# Remove leading and trailing spaces
def format_fields(record, fieldnames):
	for field in fieldnames:
		if field not in record:
			record[field] = ''
		if record[field] != None:
			record[field] = record[field].strip()

## Remove invalid json fields from input file
def remove_invalid_json_fields_from_history(input_file_name, output_file_name):
	input_file = open(input_file_name,'r', encoding='utf8')
	output_file = open(output_file_name,'w', encoding='utf8', newline='')
	for line in input_file.readlines():
		#DARPG input history file has some known json format errors. Hence dropping those attributes
		if not ('action_srno' in line or 'date_of_action' in line or 'delay' in line or 'item_no' in line):
			output_file.write(line)
	input_file.close()
	output_file.close()

def writeFinalCsv(report_data, history_dict, output_csv_file):
	# Create the csv writer object
	fieldnames = ['registration_no', 'org_code', 'dist_name', 'pincode', 'state', 'sex', 'history_id', 'history_officer_detail', 'history_org_code']
	csv_writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames)

	print('## Grievance report file is loaded')
	print("## Records in grievance file : ", len(report_data))

	# Counter variable used for writing headers to the CSV file
	count = 0
	for record in report_data:
		if count == 0:
			count += 1
			csv_writer.writeheader()

		format_fields(record, fieldnames)

    	#TODO - Below hard coding of field names can be optimized further
		csv_writer.writerow({'registration_no': record['registration_no'], 
					   'org_code': record['org_code'], 'dist_name': record['dist_name'], 
					  'pincode': record['pincode'], 'state': record['state'], 'sex': record['sex'], 
					  'history_id': history_dict.get(record['registration_no'])['_id'],
					  'history_officer_detail': history_dict.get(record['registration_no'])['OfficerDetail'],
					  'history_org_code': history_dict.get(record['registration_no'])['org_code']
					  })

def main():
	print('## Starting file loads')

	#Remove invalid json elements from history file
	remove_invalid_json_fields_from_history(history_json_file_name, history_json_file_temp_name)

	with open(history_json_file_temp_name, encoding='utf8') as history_json_file:
		history_data = json.load(history_json_file)

	with open(report_json_file_name, encoding='utf8') as report_json_file:
		report_data = json.load(report_json_file)

	print('## Grievance hisory file is loaded')
	print('## Records in history_data : ', len(history_data))

	#Create a dictionary of history records. We are interested in the latest update of each grievance.
	#Assumption is that history records for grievance are in ascending order of time. So we look for last record for each grievance
	history_dict = {}
	for record in history_data:
		#Keep overwriting the same key
		history_dict[record['registration_no']] = record 
	print("## Records in history_dict : ", len(history_dict))

	# Open file for writing
	output_csv_file = open(gievance_merged_csv_file_name, 'w', encoding='utf8', newline='')
	
	writeFinalCsv(report_data, history_dict, output_csv_file)
	
	#Cleanup of open file handlers
	report_json_file.close()
	history_json_file.close()
	output_csv_file.close()

if __name__ == "__main__":
    main()



