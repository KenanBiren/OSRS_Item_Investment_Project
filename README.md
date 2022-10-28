Runescape Item Analysis: 
Providing users with item-by-item investment analysis for Runescape items.

Introduction: Brief summary of Runescape and the Grand Exchange. Examples of 
current similar products 


Project Description:

This project is built off of my previous project, which is an ELT
pipeline that performs investment analysis on Runescape item data.
Link:

This project uses data collection and analysis methods from the previous project. 
The purpose of this project is to serve users a bigger picture of investment
analysis on specific items that they are considering. To do this, users will
search for a specific item, and the analysis will be applied to that item.
Additionally, a graph displaying past-two-week price/volume interactions
and near-real time data scraped from ge-tracker.com is presented.

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

