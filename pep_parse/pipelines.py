import csv
from pathlib import Path
from collections import Counter
from datetime import datetime as dt


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_status_dict = Counter()
        self.result_dir = BASE_DIR / 'results'
        self.result_dir.mkdir(exist_ok=True)
        self.current_dt = dt.now().strftime("%Y-%m-%dT%H-%M-%S")

    def process_item(self, item, spider):
        self.pep_status_dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_dir = f'{self.result_dir}/status_summary_{self.current_dt}.csv'
        with open(file_dir, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.pep_status_dict.items())
            writer.writerow(['Total', self.pep_status_dict.total()])
