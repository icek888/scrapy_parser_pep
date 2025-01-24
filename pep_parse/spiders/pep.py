import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_SPIDER_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    # Реализовано через константу записанную в настройках
    allowed_domains = (PEP_SPIDER_URL,)
    start_urls = [f'https://{PEP_SPIDER_URL}/']

    def parse(self, response, **kwargs):
        for link in response.css(
            'tbody tr a[href^="pep-"]'
        ):
            yield response.follow(
                link, callback=self.parse_pep
            )

    def parse_pep(self, response):
        _, number, _, *name = response.css(
            'h1.page-title::text'
        ).get().split()
        data = {
            'number': number,
            'name': ' '.join(name).strip(),
            'status': response.css(
                'dt:contains("Status")+dd abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
