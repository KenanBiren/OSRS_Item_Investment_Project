# Runescape Item Investment Analysis

Providing investors with item-by-item investment analysis for Runescape items.


# Table Of Contents:
1. Introduction
           
   Purpose
3. Sources of Data
4. Backend Components
   
   Examples
6. Frontend Components

   Examples
8. Future Changes





## Introduction: 

Old School Runescape (OSRS) is an online game was realesed in February 2013 as a reboot of an old version of the game Runescape. Millions of people play the game, as it offers a wide variety of activities like going on quests, fighting monsters and other players, and levelling up your character's skills. OSRS players can trade each other items for gold coins, and the game has an automated trading system so players can buy or sell items without having to schedule a time to meet and trade.

The automated trading system is called the Grand Exchange. One player puts their item into the system, one player their coins, and it conducts the trade. Because almost all trades happen on the Grand Exchange, players often in try to observe trends in price, and invest in items that will go up. Some players make millions of coins each day by choosing the correct items. One might ask, how do they make their decision? The purpose of this project is to help an investor decide if a specific item is a good investment or not. 



## Purpose:

Investment prediction is one of the most complex topics out there, so investors need as much information as possible to make decisions. This project performs a daily market analysis of the OSRS item market, and applies that data to any item searched, predicting how much it will change in price today. Additionally, upon search for an item, data from ge-scraper.com is extracted and presented, and a graph showing the interaction between price and volume in the last two weeks is presented.

1. In the background: This daily data analysis is performed on two weeks' worth of price and volume trading data (all items).
2. When a user searches for an item, the results of this daily analysis are applied to that item to predict how much it will change in price in the next day.
3. Item is searched and data is extracted from ge-tracker.com to provide user with the most up-to-date information on that item.
4. A graph of price and volume over the past two weeks is presented. Price and volume are plotted on the same graph with different y-axes so that there interaction between the two can be viewed, as oftentimes an item's price and volume average for the day are magnitudes apart.

This project uses Python - Scrapy and Pandas - in the backend to scrape web data and analyze it. Analyzed data is sent to an S3 bucket, where it can be accessed by the frontend scripts. A file name status_file.csv is used to prevent concurrent uploads and downloads to S3, and also holds some useful fields that can be used in verification tests.





## Sources of Data:
There are many sources that give data on items that OSRS investors might want. Here are the sources of data used in this project (showing example item Abyssal Whip).


Official Old School Runescape website:
https://secure.runescape.com/m=itemdb_oldschool/Abyssal+whip/viewitem?obj=4151

This website shows the daily average price and volume per item. The daily average data from this site is what is best to use for daily investment analysis. We wouldn't want to extract near-real time data from either of the sources below and pretend as if it represents the average price that day.


Old School wiki database:
https://prices.runescape.wiki/osrs/item/4151

This site shows up-to-date price/volume data and a few other basic fields like "Buy Limit". This site is a fast API that is a great source to get a list of all items in the game, with the ability to use the API to pre-filter based on specific values (this may be utiilized in the future).


ge-tracker.com:
https://www.ge-tracker.com/item/abyssal-whip

This site shows near-real time data. This site is used because it includes unique fields like "Buying Quantity (1 hour)" and "Selling Quantity (1 hour)" which could be very useful for investors.





#### Mention: The backend of this project is based off of my [previous ELT pipeline](https://github.com/Kenan-Biren/OSRS_Investment_Project)


I made this into an entirely new project because I am not utilizing AWS Redshift any more. This game has 3841 items, so the data analysis can be handled fine with Pandas. This is better because I plan to incorporate factorial analysis in the future to replace data calculated directly from sums and averages of raw data. This should increase the accuracy of the analysis, and having all components as python scripts will make Dockerizing them much faster to do. 



## Backend Components:
    Daily Scrape
    Daily Analysis
    Processing

### Daily Scrape:

This project uses the Scrapy framework to extract data from web sources. There are two spiders, one scrapes one days' worth of data and the other scrapes two weeks' worth of data. This is in case new items are added to the game and for the very first scrape. A pre-analysis script goes along with each spider, which takes the spider output and formats to 14day_price.csv and 14day_vol.csv to prepare for analysis.




### Daily Analysis:

The daily analysis takes 14 days of raw price and volume data
for every item in game and calculates factors that can be analyzed for each item. 


Data Analysis Calculated Fields:

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


The average effect of each factor on price change is calculated by averaging recent price change (same as one_day_avg_p) across all items where that factor applies. This produces a data_summary file which lists each factor, and how much % change it is expected to make in items that have that factor. For example, if the average price change for all items with two_day_run_p=1 (True) is 2%, a specific item that has two_day_run_p=1 will be assumed to increase 2% in the next day.

When a user searches for an item, that item's factor data is multiplied by the average effect of every factor. This results in a prediction of % price increase (or decrease).










## Frontend Components:
    Read User Input
    Update Analysis Data
    Serve Analysis Data
    Serve Near-real Data

### Read User Input: 

User is prompted to search for an item. If an item match is not found from the master list, the user is asked if they meant "...". 

### Update Analysis Data: 

After a user input is matched to an item name, local filesystem is checked to see if the data has been updated today. If not, download it from S3 and use the updated data.

### Serve Analysis Data: 

Use Pandas library to multiply item name's analysis table data with today's data summary, giving a prediction for how much it will go up in price within the next day. Create a graph for that item comparing price and volume data for the past two weeks.


### Serve Near-real Data: 
The near-real time data presented to the user is scraped on-demand from ge-tracker.com. 


    Current Price: ... (average price item being bought/sold at)

    Current Sell Price: ... (price sellers are placing their item)

    Current Offer Price: ... (price buyers are offering for item)

    Selling Quantity (1 hour): ... (amount being placed up for sale)

    Buying Quantity (1 hour): ... (amount being sold)

    Buy/Sell Ratio: ... (bought per hour/sold per hour)

    Tax: ... (tax on seller)

    Buy Limit: (limit within 4 hour cap)


#### There is a difference between buy and sell prices because the Grand Exchange works as a double auction. 




## Future Changes:

v1.1.0 : Replace Selenium package with requests or other library more compatible with Docker

v1.2.0 : Dockerize frontend components

v1.3.0 : Dockerize backend components

v2.0.0 : Incorporate factorial design in daily analysis

v3.0.0 : Add user interface
