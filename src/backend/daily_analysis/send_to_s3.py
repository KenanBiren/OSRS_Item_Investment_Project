This script is the final step in process_backed.py. It takes all the
results of the analysis and sends them to a folder in s3 labeled 
today's date




triggered by: process_backend.py

next task: -

inputs: none (contents taken from 14day_price.csv and 14day_vol.csv

outputs: sends folder titled *current date* containing /data folder contents
to s3

data storage used: s3, EC2 local (Docker /data volume)

test scripts needed: