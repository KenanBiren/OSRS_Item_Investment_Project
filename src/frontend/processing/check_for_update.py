This script runs right after a user searches for an item. It checks
if the daily analysis data has been updated, downloads it from s3 if 
it is ready to be updated









# Get current date
# Check if local /Data/ folder was updated today
# If yes:
#   continue to serve data
#else:
#   download status_file from S3 and check if analysis is running
#   If it is:
#       print("Daily analysis is currently processing, please try
#              again in 10 seconds")
#       return to start of app
#   else:
#       print("Daily Investment analysis not yet updated. Please check
#              again soon for more accurate information.")
#       continue to serve data



