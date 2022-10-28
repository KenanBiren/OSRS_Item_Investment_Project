This script creates analysis_table.csv from the pre-formatted
14day_price.csv and 14day_vol.csv



triggered by: process_backend.py

next task: create_data_summary.py

inputs: 14day_price.csv and 14day_vol.csv
(from full_pre_analysis or incr_pre_analysis)

outputs: analysis_table.csv

data storage used: EC2 local (Docker /data volume)

test scripts needed: