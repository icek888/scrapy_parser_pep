import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        # Проходим по всем таблицам с PEP
        for table in response.css('section table.pep-zero-table'):
            # Проходим по всем строкам таблицы
            for row in table.css('tbody tr'):
                # Извлекаем статус из атрибута title элемента <abbr>
                status = row.css('td:nth-child(1) abbr::attr(title)').get()
                # Извлекаем номер PEP
                pep_number = row.css('td:nth-child(2) a::text').get()
                # Извлекаем название PEP
                pep_name = row.css('td:nth-child(3) a::text').get()

                # Если статус не найден, используем значение по умолчанию
                if not status:
                    status = 'Unknown'

                # Создаём объект PepParseItem
                yield PepParseItem(
                    number=pep_number,
                    name=pep_name,
                    status=status,
                )

    def parse_pep(self, response):
        pass
