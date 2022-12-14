import scrapy
from scrapy.http import FormRequest
from ..items import IncrScrapeItem
import datetime
from scrapy import Request


class IncrScrapeSpider(scrapy.Spider):
    name = 'incr_spider'
    def start_requests(self):
        with open('~OSRS_Item_Investment_App/data/item_links.csv') as f:
            for line in f:
                line = line.strip()
                if len(line.strip('"')) == 0:
                    continue
                yield Request(url=line)


    def parse(self, response, **kwargs):
        price_list = []
        volume_list = []
        ind = 0
        fields = ['name', 'price', 'volume']
        items = OsrsExtractItem()
        names = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "item-description", " " ))]//h2/text()').extract()
        name = names[0]
        data = response.xpath('//*[@id="grandexchange"]/div/div/main/div[2]/script').get()
        all_lines = data.splitlines()
      





        current_date = datetime.date.today()  ## Get date two weeks ago
        curr_str = current_date.strftime('%Y/%m/%d')
        yest_date = current_date - datetime.timedelta(days=1)
        yest_str = yest_date.strftime('%Y/%m/%d')
        #curr_str = yest_str  ## COMMENT OUT THIS LINE IN PRODUCTION, ALLOWS FOR
                               ## TESTING WHEN OSRS WEBSITE DATA ISN'T UPDATED
        
        
        for i in range(len(all_lines)):
            if yest_str in all_lines[i]:  ## Use past date to find starting index for parsing
                ind = i
                break
  
        ind = ind + 2

        line_text = all_lines[ind]  ## Extract price data
        split = line_text.split(", ")
        price = ''.join(filter(str.isdigit, split[1]))
        ind = ind + 1

        line_text = all_lines[ind]  ## Extract volume data
        split = line_text.split(", ")
        volume = ''.join(filter(str.isdigit, split[1]))
        
        items['name'] = name
        items['price'] = price 
        items['volume'] = volume

        yield items