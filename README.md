Runescape Item Investment Analysis

Providing users with item-by-item investment analysis for Runescape items.



Introduction: 

Old School Runescape (OSRS) is an online game was realesed in February 2013 as a reboot of an old version of the game Runescape. Millions of people play the game, as it offers a wide variety of activities like going on quests, fighting monsters and other players, and levelling up your character's skills. OSRS players can trade each other items for gold coins, and the game has an automated trading system so players can buy or sell items without having to schedule a time to meet and trade.

The automated trading system is called the Grand Exchange. One player puts their item into the system, one player their coins, and it conducts the trade. Because almost all trades happen on the Grand Exchange, players often in try to observe trends in price, and invest in items that will go up. Some players make millions of coins each day by choosing the correct items. One might ask, how do they make their decision? The purpose of this project is to tell an investor if a specific item is a good investment or not. 


There are many sources that give data on items that investors might want. Here are the sources of data for this project (opened on example item Abyssal Whip).


Official Old School Runescape website:
https://secure.runescape.com/m=itemdb_oldschool/Abyssal+whip/viewitem?obj=4151
This website shows the daily average price and volume per item. The average daily value is what is best to perform data analysis on the past week, two weeks, or month worth of data, if that is the plan (it is).


Old School wiki database:
https://prices.runescape.wiki/osrs/item/4151
This site shows up-to-date price/volume data and a few other basic fields like "Buy Limit". This site is a fast API that is a great source to get a list of all items in the game, with the ability to use the API to pre-filter based on specific values (this may be utiilized in the future).


ge-tracker.com:
https://www.ge-tracker.com/item/abyssal-whip
This site shows up-to-date data and also includes unique fields like "Buying Quantity (1 hour)" and "Selling Quantity (1 hour)"

As you can see, each of these sources provides something a little different. Investment prediction is one of the most complex topics out there, so investors need as much information as possible to make decisions. This project performs a daily market analysis of the OSRS item market, and 
applies that data to any item searched, predicting how much it will change in price today. Additionally, upon search for an item, data from ge-scraper.com is extracted and presented, and a graph showing the interaction between price and volume in the last two weeks is presented.

The daily market analysis section is based off of my previous ELT pipeline. 
link:
I made this into an entirely new project because I am not utilizing AWS Redshift or Eventbridge any more. The previous project was great for getting my feet wet and learning about AWS: moving data across softwares, using access control policies, etc. But this game only has 3841 items, it doesn't need Redshift. Investors, however, need a broad view of each potential investment. As such, I nixed Redshift and shifted focus towards building an app. 


examples of outputs:
images




Project Structure: architecture diagrams




Backend:

Daily Data Extraction: ...

Daily Data Analysis: The daily analysis takes 14 days of raw price and volume data
for every item in game and calculates factors that can be analyzed for each item. 

Data Analysis Calculated Fields:

two_day_run_p = whether daily trading price has increased consecutively past two days
two_day_run_v = whether daily volume has increased consecutively past two days
three_day_run_p = ...   past three days
three_day_run_v = ...
five_day_run_p = ...
five_day_run_v = ...
seven_day_run_p = ...
seven_day_run_v = ...

one_day_avg_p = increase (or decrease) in daily average price compared to yesterday
one_day_avg_v = increase (or decrease) in volume compared to yesterday
three_day_avg_p = ...    compared to three days ago
three_day_avg_v = ...
seven_day_avg_p = ...
seven_day_avg_v = ...
fourteen_day_avg_p = ...
fourteen_day_avg_v = ...


The effect of each factor on price change is calculated by averaging recent price
change (same as one_day_avg_p) across all items where that factor applies. When a 
user searches for an item through the interface, that items factor data is
multiplied by the average effect of each factor. 

I chose to do it this way because I intend to improve this analysis in the 
future with a proper factorial design experiment. 



Frontend:

Analysis Data: Analysis data produced daily is applied to the item searched by
user




            Price/volume graphs: Data is taken from 14-day price and volume data and
            plotted on the same plot with a unique y axis for each. This allows us to
            visualize any recent strong interactions between price and volume. 





Near-real time data: The near-real time data presented to the user is scraped
on-demand from ge-tracker.com. 

Fields:

Current Price: ... (average price item being bought/sold at)
Current Sell Price: ... (price sellers are placing their item)
Current Offer Price: ... (price buyers are offering for item)
Selling Quantity (1 hour): ... (amount being placed up for sale)
Buying Quantity (1 hour): ... (amount being sold)
Buy/Sell Ratio: ... (bought per hour/sold per hour)
Tax: ... (tax on seller)
Buy Limit: (limit within 4 hour cap)

















This is why I chose what information to show the user.


Overview of current options for runescape item prediction:
    official website
    ge-tracker.com
    wiki database
    phone apps

    pros and cons

Why I thought of factorial analysis



Future features:
Docker Compose
Factorial analysis
User interface

