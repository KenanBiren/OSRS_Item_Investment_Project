This script combines app components




1. Call read_user_input, which will return an item_name
2. Call check_for_update.py, which will update data from S3 if needed
3. Call serve_analysis_data() to output analysis data and graph for item_name
4. Call serve_near_real_data to output near-real time data for item_name
5. Repeat