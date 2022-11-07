import csv






# start location is project folder, checks analysis_table and data_summary
analysis_row_check = False
analysis_col_check = False
analysis_val_check = False

summary_row_check = False
summary_col_check = False
summary_val_check = False

check_list = []

with open("data/analysis_table.csv", "r") as f:
    reader = csv.reader(f)
    num_rows = 0
    for row in reader:              # check number of rows
        num_rows = num_rows + 1
    if num_rows > 1500:
        analysis_row_check = True

    reader = csv.reader(f)
    head_row = next(reader)         # check name of header
        if head_row[1] == 'two_day_run_p':
            analysis_col_check = True
    try:
        next_row = next(reader)
        value = next_row[1]         # check for non-null value in 2nd row
            if len(str(value)) > 0:
                analysis_val_check = True
    except:
        continue
    f.close()






with open("data/data_summary.csv", "r") as f:
    reader = csv.reader(f)
    num_rows = 0
    for row in reader:              # check number of rows
        num_rows = num_rows + 1
    if num_rows > 1:
        summary_row_check = True

    reader = csv.reader(f)
    head_row = next(reader)         # check name of header
        if head_row[1] == 'two_day_run_p':
            summary_col_check = True
    try:
        next_row = next(reader)
        value = next_row[1]         # check for non-null value in 2nd row
            if len(str(value)) > 0:      
                summary_val_check = True
    except:
        continue
    f.close()



check_list = [analysis_row_check, analysis_col_check, analysis_val_check,
                summary_row_check, summary_col_check, summary_val_check]

for check in check_list:
    if check == False:
        raise Exception("post_scrape_test.py FAILED")