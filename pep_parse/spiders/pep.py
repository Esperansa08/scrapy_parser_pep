import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.xpath('//*[@id="numerical-index"]')
        tbody = all_pep.css('tbody')
        href_pep = tbody.css('a[href^="pep"]')
        for pep_link in href_pep:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        text = response.css('h1.page-title::text').get().split()
        data = {
            'number': int(text[1]),
            'name': " ".join(text[3:]),
            'status': response.css('dd').css('abbr::text').get()}
        yield PepParseItem(data)
