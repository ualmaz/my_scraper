import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    
    def start_requests(self):
        a = ['https://shailoo.gov.kg/media/shamenov/2017/10/21/5338_RvnE5Ns.pdf']
        # a = list(map('https://shailoo.gov.kg/media/shamenov/2017/10/21/{}.pdf'.format, range(5274, 5327)))
        # urls = ['https://shailoo.gov.kg/media/elia/2017/10/21/8186.pdf']
        for url in a:
            yield scrapy.Request(url=url, callback=self.parse)
            # print(url)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'Ошская территориальная избирательная комиссия7-%s.pdf' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

