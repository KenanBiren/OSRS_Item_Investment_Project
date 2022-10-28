This script creates data summary values from the analysis_table.csv 



triggered by: process_backend.py

next task: send_to_s3

inputs: analysis_table.csv produced from daily_analysis.py

outputs: data_summary.csv 

data storage used: EC2 local (Docker /data volume)

test scripts needed: