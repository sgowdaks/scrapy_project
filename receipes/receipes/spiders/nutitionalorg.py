from urllib.parse import urljoin
from scrapy import Selector
import scrapy
import requests

class NutritinalOrg(scrapy.Spider):
    name = 'nutrition' # name of spider
	
    start_urls = ['https://www.nutritionvalue.org/search.php?food_query=BOLTHOUSE+FARMS']

    def parse(self, response):
        product = []
        url = "https://www.nutritionvalue.org/search.php?food_query=BOLTHOUSE+FARMS"
        product.append(url)
        # for i in range(2, 3):
        #     url_ = url + "&page=" + str(i)
        #     product.append(url_)

        print(product)

        for items in product:
            yield scrapy.Request(items, callback=self.parse_page)
         

    def parse_page(self, response):
        item = response.xpath("//td/table/tbody/tr/td[contains(@class, 'left')]/a/@href").extract()
        print(item)

    #     yield scrapy.Request(item, callback=self.receipe)

    # def receipe(self, response):
    #     ingredients_ = response.xpath("//ul[contains(@class, 'wprm-recipe-ingredients')]/li")
    #     title =  response.xpath("//td/h1/text()").extract()
    #     # image = response.xpath("//img[contains(@class,'image')]/@src").extract()[2]
    #     # if len(image) < 2:
    #     # image =  response.xpath("//img[contains(@class,'image')]/@src").extract()[2]
    #     ingredient = []
    #     for ingredient_ in ingredients_:
    #         s = ' '.join(ingredient_.xpath(".//text()").extract())
    #         ingredient.append(s.strip())

    #     if len(title) == 1 and ingredient != "":
    #         yield {
    #             "name": title,
    #             "ingredients": ingredient,
    #             "image_url": None
    #          }

