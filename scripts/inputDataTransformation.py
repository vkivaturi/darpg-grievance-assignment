import sys
#Copy specific number of rows from one CSV to another
#Perform data cleaning and other transfrmation rules
input_filename_csv = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\grievance_merged_history_full.csv'
output_filename_csv = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\grievance_merged_history_full_truncated.csv'

rows_to_copy = int(sys.argv[1])

def copy_odd_lines(input_file, output_file, rows_to_copy):
    with open(input_file, 'r', encoding='utf8') as infile, open(output_file, 'w', encoding='utf8', newline='') as outfile:
        for line_number, line in enumerate(infile, 1):
            if line_number < rows_to_copy:
                outfile.write(line)
                #Convert all rows to upper case
#                lineUC = line.upper()
#                if (lineUC.strip().endswith('M')) or (lineUC.strip().endswith('F') or line_number ==1):
#                    outfile.write(lineUC)

copy_odd_lines(input_filename_csv, output_filename_csv, rows_to_copy)