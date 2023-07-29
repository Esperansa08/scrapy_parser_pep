import scrapy

from pep_parse.items import PepParseItem
from settings import NAME_SPYDER, ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = NAME_SPYDER
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_pep = response.xpath('//*[@id="numerical-index"]')
        tbody = all_pep.css('tbody')
        href_pep = tbody.css('a[href^="pep"]')
        for pep_link in href_pep:
            yield response.follow(f'{pep_link}/', callback=self.parse_pep)

    def parse_pep(self, response):
        text = response.css('h1.page-title::text').get().split()
        data = {
            'number': int(text[1]),
            'name': " ".join(text[3:]),
            'status': response.css('dd').css('abbr::text').get()}
        yield PepParseItem(data)
