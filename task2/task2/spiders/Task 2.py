

import scrapy


class Forbes(scrapy.Spider):

    name = "Forbes2000"



    start_urls = [
        'https://www.forbes.com/lists/global2000/?sh=6ebe82ee5ac0',

    ]

    def parse(self, response):
        for link in response.css("div.table-row-group a::attr(href)")[0:20]:

            yield response.follow(link.get(), callback=self.parse_allcompany)

    def parse_allcompany(self,response):
        products = response.css('div.listuser-header__name')
        for products in products:
            yield {
                'Name': products.css('div.listuser-header__name::text').extract(),
            }
        products1 = response.css('div.listuser-header__headline--premium-location')
        for products1 in products1:
            yield {
                'Location': products1.css('div.listuser-header__headline--premium-location::text').extract()
            }
        products2 = response.css('div.listuser-content__bio--shortened')
        for products2 in products2:
            yield {
                'About': products2.css('div.listuser-content__bio--shortened::text').extract()
            }

