This script runs weekly (when "Week of XXXX/XX/XX" folders are formatted).
It scrapes the full item list from the wiki database and compares its length
to the data stored locally. If new items are detected, new_items.csv is edited
to indicate such (leading to new_item_trigger = True in process_backend.py)