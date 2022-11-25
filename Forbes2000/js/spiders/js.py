import scrapy


class Forbes(scrapy.Spider):
    # name of variable should be 'name' only
    name = "Forbes2000"

    # urls from which will be used to extract information
    # list should be named 'start_urls' only
    start_urls = [
        'https://www.forbes.com/lists/global2000/?sh=6ebe82ee5ac0m'
    ]

    def parse(self, response):
        # handle the response downloaded for each of the
        # requests made should be named 'parse' only
        for Forbes2000 in response.css('div.table-row-group'):
            yield {
                'rank': Forbes2000.css('.rank::text').get(),
                'name': Forbes2000.css('.name::text').get(),
                'country': Forbes2000.css('.country::text').get(),
                'sales': Forbes2000.css('.sales::text').get(),
                'profit': Forbes2000.css('.profit::text').get(),
                'assests': Forbes2000.css('.assets::text').get(),
                'marketvalue': Forbes2000.css('.value::text').get(),
                'link' : Forbes2000.css("div.table-row-group a").xpath("@href")[0].extract()
            }
