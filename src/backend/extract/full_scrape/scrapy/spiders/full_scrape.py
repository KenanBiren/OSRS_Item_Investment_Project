import scrapy
from scrapy.http import FormRequest
from ..items import FullScrapeItem
import datetime
from scrapy import Request



class FullScrapeSpider(scrapy.Spider):
    name = 'full_scrape'
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
        fields = ['name', 'p_0', 'p_1', 'p_2', 'p_3', 'p_4', 'p_5', 'p_6',
                  'p_7', 'p_8', 'p_9', 'p_10', 'p_11', 'p_12', 'p_13', 'p_14',
                  'dv_0', 'dv_1', 'dv_2', 'dv_3', 'dv_4', 'dv_5',
                  'dv_6', 'dv_7', 'dv_8', 'dv_9', 'dv_10', 'dv_11',
                   'dv_12', 'dv_13', 'dv_14']
        items = OsrsExtractItem()
        names = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "item-description", " " ))]//h2/text()').extract()
        name = names[0]
        data = response.xpath('//*[@id="grandexchange"]/div/div/main/div[2]/script').get()
        all_lines = data.splitlines()
  





        current_date = datetime.date.today()  ## Get date two weeks ago
        curr_str = current_date.strftime('%Y/%m/%d')
        past_date = current_date - datetime.timedelta(days=14)
        past_str = past_date.strftime('%Y/%m/%d')
        yest_date = current_date - datetime.timedelta(days=1)
        yest_str = yest_date.strftime('%Y/%m/%d')
        #curr_str = yest_str  ## COMMENT OUT THIS LINE IN PRODUCTION, ALLOWS FOR
                               ## TESTING WHEN OSRS WEBSITE DATA ISN'T UPDATED
       
        
        for i in range(len(all_lines)):
            if past_str in all_lines[i]:  ## Use past date to find starting index for parsing
                ind = i
                break
       
        while curr_str not in all_lines[ind]:
            line_text = all_lines[ind]  ## Extract price data
            split = line_text.split(", ")
            
            price = ''.join(filter(str.isdigit, split[1]))
            price_list.append(int(price))
            ind = ind + 1

            line_text = all_lines[ind]  ## Extract volume data
            split = line_text.split(", ")
            
            volume = ''.join(filter(str.isdigit, split[1]))
            volume_list.append(int(volume))
            ind = ind + 1

        line_text = all_lines[ind]  ## Extract price data
        split = line_text.split(", ")
        price = ''.join(filter(str.isdigit, split[1]))
        price_list.append(int(price))
        ind = ind + 1

        line_text = all_lines[ind]  ## Extract volume data
        split = line_text.split(", ")
        volume = ''.join(filter(str.isdigit, split[1]))
        volume_list.append(int(volume))
        ind = ind + 1
        price_list.reverse()
        volume_list.reverse()
        master_list = [name] + price_list + volume_list
        
        #price list volume list now from today to two weeks ago
        for i in range(len(fields)):
            items[(fields[i])] = master_list[i]

        yield items
    