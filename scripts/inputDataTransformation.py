import sys

input_filename_csv = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_grievance.csv'
output_filename_csv = 'C:\\Users\\vijay\\Downloads\\problem_statement_1_and_2\\no_pii_grievance_truncated.csv'

rows_to_copy = int(sys.argv[1])

def copy_odd_lines(input_file, output_file, rows_to_copy):
    with open(input_file, 'r') as infile, open(output_file, 'w', encoding='utf8', newline='') as outfile:
        for line_number, line in enumerate(infile, 1):
            if line_number < rows_to_copy:
                #Convert all rows to upper case
                lineUC = line.upper()
                if (lineUC.strip().endswith('M')) or (lineUC.strip().endswith('F') or line_number ==1):
                    outfile.write(lineUC)

copy_odd_lines(input_filename_csv, output_filename_csv, rows_to_copy)