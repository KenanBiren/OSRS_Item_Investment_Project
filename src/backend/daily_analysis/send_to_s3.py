






1. send local /data/ folder to s3 /data/
2. send local /data/ to local folder for today's data ~/xxxx/xx/xx/

2. if new_week_trigger:
       upload week folder to s3

       reformat/rename local stored data
            create new folder titled "next week start date" value from status file
            delete folder titled "current week start date" value from status file
       update week start dates in status_file.csv (this will reset new_week_trigger)
       trigger weekly_scrape.py

3. upload status_file.csv to s3
