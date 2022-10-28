This script is responsible for reading triggers and kicking off all backend
components




0. get current date time (this is start of scrape)
1. read if new_item_trigger is true or false based on contents of new_items.csv
2. A. if true: run full (14-day) scrapy spider
               run full (14-day) pre-analysis
   B. if false: run incremental (1-day) scrapy spider
                run incr (1-day) pre-analysis
3. get current date time (this is end of scrape and start of analysis)
4. download status_file from s3 and edit scrape start/end, next scrape date,
analysis start, analysis running = y
5. reupload status_file to s3
6. trigger analysis script
7. trigger data summary script
8. save /data folder to /Week of XXXX.XX.XX/xxxx.xx.xx on ec2
9. upload today's /Week of X/day to s3 folder with same name
10. if next scrape date = next week starting, delete /Week of X/ folder on ec2,
and create next /Week of X/ folder, run weekly link scrape
11. edit status_file with end of analysis time, analysis running = n, 
(change current week started: and next week starting: if applicable)
12. edit new_items.csv to reset new item trigger
