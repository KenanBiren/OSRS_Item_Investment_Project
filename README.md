# Runescape Item Investment Analysis

Providing investors with item-by-item investment analysis for Runescape items.
 

# Table Of Contents:
1. Introduction
2. Purpose
3. Demonstration
4. Sources of Data
5. Backend Component (Daily ETL)
6. Frontend Component (App)
7. Scheduling and CI/CD Workflow
8. Completed and Future Improvements





## Introduction: 

Old School Runescape (OSRS) is an online game released in February 2013 as a reboot of the 2007 version of Runescape. Millions of people play the game, as it offers a wide variety of activities like going on quests, fighting monsters and other players, and leveling up your character's skills. OSRS players can trade each other items for gold coins, and the game has an automated trading system so players can buy or sell items without having to schedule a time to meet and trade.

The automated trading system is called the Grand Exchange. One player puts their item into the system, one player their coins, and it conducts the trade. Because almost all trades happen on the Grand Exchange, players often in try to observe trends in price, and invest in items that will go up. Some players make millions of coins each day by choosing the correct items. 

How do they choose which items to invest in?



## Purpose:

The purpose of this project is to help an investor decide if a specific item is a good investment or not. Investment prediction is one of the most complex topics out there, so investors need as much information as possible to make decisions. This project aims to be a multifaceted investment analysis tool that gives investment analysis on an item-by-item basis. It does so by applying that specific item's data to a daily running investment analysis, and serving the results alongside the most current data (I'm calling it near-real-time data, taken from ge-tracker.com).

The purpose of all this is to provide a picture that takes into account the item's historical data on the week, day, and minute-by-minute level. These are the general steps that are taken to accomplish this.

1. Two weeks' worth of price and volume data is scraped daily with Scrapy and Pandas is used to calculate 16 data points for each item.
``` 
If the item has changed in (price, volume)
    consecutively in the past (2, 3, 5, 7) days
How much the item has changed in (price, volume)
    compared to (1, 3, 7, 14) days ago
```

3. The daily analysis is automatically sent to the "App Server" that the user interacts with.
4. When a user searches for an item, the results of this daily analysis are applied to that item to predict how much it will change in price in the next day.
5. Item name is searched and data is extracted from ge-tracker.com to provide user with the most up-to-date information on that item.
6. A graph of price and volume over the past two weeks is presented. Price and volume are plotted on the same graph to show possible trends in interactions.

This project uses Python (Scrapy and Pandas) on an EC2 instance to scrape web data and analyze it. Analyzed data is sent to an S3 bucket, where it can be accessed by the frontend scripts. A file name status_file.csv is used to prevent concurrent upload and download request to S3, and also holds some useful fields that can be used in verification tests.





## Sources of Data:
There are many sources that give data on items that OSRS investors might want. Here are the sources of data used in this project (showing example item Abyssal Whip).


Official Old School Runescape Website:
https://secure.runescape.com/m=itemdb_oldschool/Abyssal+whip/viewitem?obj=4151

This website shows the daily average price and volume per item. This source gives daily average data for each item, unlike the next two sources which give near-real-time data. Therefore this website is used as the data source for the daily-running investment analysis.


Old School Wiki Database:
https://prices.runescape.wiki/osrs/item/4151

This site shows up-to-date price/volume data and a few other basic fields like "Buy Limit". This site is a fast API that is a great source to get a master list of all items in the game, with the ability to use the API to pre-filter based on specific values (this may be utiilized in the future).


ge-tracker.com:
https://www.ge-tracker.com/item/abyssal-whip

This site shows near-real time data. This site is similar to the Wiki API, but is used because it includes other data fields such as "Buying Quantity (1 hour)" and "Selling Quantity (1 hour)" which could be very useful information for users.


## Backend Component (Daily ETL):
    Daily Scrape
    Daily Analysis
    Processing


#### Mention: The backend of this project is based off of my [previous ELT pipeline](https://github.com/Kenan-Biren/OSRS_Investment_Project)


A major goal of that project was to develop more experience with using cloud technologies (AWS) in a data pipeline. Upon finishing that project, I wanted to implement a CI/CD workflow specifically with Github and Docker, but I didn't really know what improvements I wanted to implement.
After some thought I realized that I could make this a lot more interesting by providing users an item-by-item analysis instead of a general daily recommendations list. Having a more defined focus for the end product has allowed me to easily think ahead to what features users might want, and decide how to restructure the project to leverage the use of Github and Docker in a CI/CD workflow.




### Daily Scrape:

This project uses the Scrapy framework to extract data from web sources. There are two spiders, one scrapes one days' worth of data and the other scrapes two weeks' worth of data. The two week spider is for when new items are added to the game and for the very first scrape. A pre-analysis script goes along with each spider, which takes the spider output and formats to 14day_price.csv and 14day_vol.csv to prepare for analysis.
14day_price.csv and 14day_vol.csv contain the past 14 days of price and volume data for all items, indexed by correct dates.



### Daily Analysis:

The daily analysis takes 14 days of raw price and volume data for every item in game and calculates attributes that can be analyzed for each item. 


Data Analysis Calculated Attributes:

    two_day_run_p = whether daily trading price has increased consecutively in the past two days. 1 = True, 0 = False
    two_day_run_v = whether daily volume has increased consecutively in the past two days. 1 = True, 0 = False
    three_day_run_p = ...                                                   past three days 
    three_day_run_v = ...
    five_day_run_p = ...
    five_day_run_v = ...
    seven_day_run_p = ...
    seven_day_run_v = ...

    one_day_avg_p = increase (or decrease) in daily average price compared to yesterday
    one_day_avg_v = increase (or decrease) in volume compared to yesterday
    three_day_avg_p = ...                            compared to three days ago
    three_day_avg_v = ...
    seven_day_avg_p = ...
    seven_day_avg_v = ...
    fourteen_day_avg_p = ...
    fourteen_day_avg_v = ...


The average effect of each attribute on price change is calculated by averaging recent price change (same as one_day_avg_p) across all items where that factor applies. This produces a data_summary file which lists each attribute, and how much % change it is expected to make in items that have that attribute. For example, if the average price change for all items with two_day_run_p=1 (True) is 2%, a specific item that has two_day_run_p=1 will be assumed to increase 2% in the next day.

When a user searches for an item, that item's attribute data is multiplied by the average effect of every factor. This results in a prediction of % price increase (or decrease).


### Processing:

Every day data is scraped from the web to prepare for analysis. Most of the time only one day's worth of data is collected and prepared for analysis. But if new items are added to the game, or the pipeline needs to start for the first time, two weeks' worth of data is collected and prepared for analysis. Once data is ready for analysis, the backend signals that data analysis has started by editing and uploading the status file to S3.

Data analysis is triggered which produces today's analysis table and data summary. All files pertaining to today's data are saved in appropriate folders, then uploaded to S3 for use by the frontend. If tomorrow is the start of the next week, the folder for this week's data is also uploaded to S3, and the weekly scrape is triggered to check if new items have been added to the game.

To finish everything off, the status file is uploaded to S3 to signal that the daily analysis is done, and new data is ready to be downloaded. 





## Frontend Component (App):
    Read User Input
    Update Analysis Data
    Serve Analysis Data
    Serve Near-real Data

### Read User Input: 

User is prompted to search for an item. If no item matches, the user given a list of item names that they might have been trying to spell.

### Update Analysis Data: 

After a user input is matched to an item name, local filesystem is checked to see if the data has been updated today. If not, download it from S3 and use the updated data.

### Serve Analysis Data: 

Pandas library is used to multiply item name's analysis table data with today's data summary, giving a prediction for how much it will go up in price within the next day. A graph is created comparing that item's price and volume data for the past two weeks.


| Attribute  | Has Effect? | Effect
| ------------- | ------------- | ------------- |
| two_day_run_p  | Yes  | 0.00432 |
| three_day_run_p  | Yes  | 0.01030 |
| five_day_run_p  | Yes  | 0.02335 |
| seven_day_run_p  | No  | 0 |
| two_day_run_v  | No  | 0 |
| three_day_run_v  | No  | 0 |
| five_day_run_v  | No  | 0 |
| seven_day_run_v  | No  | 0 |
| one_day_avg_p  | Yes  | 0.00198 |
| three_day_avg_p  | Yes  | -0.00198 |
| seven_day_avg_p  | Yes  | -0.00093 |
| fourteen_day_avg_p  | Yes  | -0.00154 |
| one_day_avg_v  | Yes  | 0.00116 |
| three_day_avg_v  | Yes  | -0.00011 |
| seven_day_avg_v  | Yes  | 0.00069 |
| fourteen_day_avg_v  | Yes  | 0.00057 |
| Total |  | 3.781% |

<img width="638" alt="price_volume_graph" src="https://user-images.githubusercontent.com/116853630/198848946-8671cc9a-c59a-4a06-914d-1e3a10bb4b7f.png">


### Serve Near-real Data: 
The near-real time data presented to the user is scraped on-demand from ge-tracker.com using Selenium.


    Current Price: 1,554,956 (average price item being bought/sold at)

    Current Sell Price: 1,567,979 (price sellers are placing their item)

    Current Offer Price: 1,545,259 (price buyers are offering for item)

    Selling Quantity (1 hour): 74 (amount being placed up for sale)

    Buying Quantity (1 hour): 84 (amount being sold)

    Buy/Sell Ratio: 1.14 (bought per hour/sold per hour)

    Tax: -15,679 (tax on seller)

    Buy Limit: 70 (limit within 4 hours)

   
#### Note: There is a difference between buy and sell prices because the Grand Exchange works as a double auction. 


## Completed and Future Improvements:
~~v1.0.0~~ : Completed first project version with functional scripts (no Docker or Airflow)

~~v2.0.0~~ : Dockerized project and implemented CI/CD workflow
```
Restructured project repository for ease of implementing Docker

Rewrote Python scripts using the Selenium package to use Requests instead (Selenium + Docker is a headache)

Added Dockerfiles for project components in /build/ folder

Implemented Github workflows to automatically build, verify, and send Docker images to Docker Hub (from Github "test" and "main" branches)

Set up Airflow DAGs to automatically delete old Docker resources and pull the appropriate images from Docker Hub before runtime

Eliminated the use of Amazon Simple Storage Service (S3) to improve runtime efficiency and make it easier for others to run this project

        - Deleted scripts / functions that interacted with S3
        - Docker images utilize bind mounts, backend-frontend file transfer is now handled in one operation with Airflow STFPOperator
        - Replaced any lost backend functionalities with new scripts (set_scrape_type.py, trigger_scrape.py)
        
Added basic runtime test scripts for backend (post_scrape_test.py, analysis_test.py)
```


v2.1.0 : Complete 100% coverage of runtime unit and integration tests (~75% done)

v3.0.0 : Implement a user interface
