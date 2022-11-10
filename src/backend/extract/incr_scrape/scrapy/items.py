# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# these are the indexes for data scraped by the incremental (1-day) spider
# this data is combined with yesterday's data by post_scrape.py to create
# 14day_price.csv and 14day_vol.csv files
class IncrScrapeItem(scrapy.Item):
    
    name = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()


    pass
