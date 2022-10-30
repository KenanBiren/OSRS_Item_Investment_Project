import scrapy




# these are the indexes for data scraped by the incremental (1-day) spider
# these indexes are converted to dates by pre_analysis
class IncrScrapeItem(scrapy.Item):

    name = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()
   
    pass