import time
import requests
import datetime


# this script goes to the OSRS website to read if today's data was updated
# if today's data is not up, wait 10 minutes
# when it has been updated, continue to next script (scrape)

def start_scrape():

    ready_to_continue = False
    current_date = datetime.date.today()
    current_date_str = current_date.strftime('%Y/%m/%d')
    while ready_to_continue ==  False:
        url = 'https://secure.runescape.com/m=itemdb_oldschool/Abyssal+whip/viewitem?obj=4151'
        head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

            # get html lines of webpage 
        response = requests.get(url, headers=head)
        old_lines = response.content.splitlines()
        new_lines = []

            # separate lines of html into a list
        for i in range(len(old_lines)):
            new_lines.append(str(old_lines[i]))

        for l in range(len(new_lines)): # search list of lines for update entry with today's date
            if new_lines[l].__contains__("[new Date('%s')" % current_date_str):
                ready_to_continue = True
        if ready_to_continue == False:
            time.sleep(600)


start_scrape()

print('Scrape ready to start. Starting...')
