import scrapy





class IncrScrapeItem(scrapy.Item):

    name = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()
   
    pass