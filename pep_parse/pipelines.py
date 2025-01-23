# pipelines.py
import os
from collections import defaultdict
import csv


class PepParsePipeline:
    def open_spider(self, spider):
        # Создаём директорию results, если её нет
        os.makedirs('results', exist_ok=True)
        # Словарь для подсчёта количества PEP по статусам
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        # Увеличиваем счётчик для текущего статуса
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        # Формируем имя файла с временной меткой
        timestamp = spider.crawler.stats.get_value('start_time').strftime(
            '%Y-%m-%d_%H-%M-%S')
        filename = f'results/status_summary_{timestamp}.csv'

        # Сохраняем сводку в файл
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            total = 0
            for status, count in self.status_counts.items():
                writer.writerow([status, count])
                total += count
            writer.writerow(['Total', total])
