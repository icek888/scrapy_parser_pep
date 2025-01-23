# items.py
import scrapy


class PepParseItem(scrapy.Item):
    number = scrapy.Field()  # Номер PEP
    name = scrapy.Field()    # Название PEP
    status = scrapy.Field()  # Статус PEP
