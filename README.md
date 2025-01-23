# Scrapy Parser PEP

Этот проект представляет собой асинхронный парсер документов PEP (Python Enhancement Proposals) с использованием фреймворка Scrapy. Парсер собирает информацию о всех PEP и сохраняет её в два CSV-файла:
1. Список всех PEP с номерами, названиями и статусами.
2. Сводка по статусам PEP с количеством документов в каждом статусе.

---

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/scrapy_parser_pep.git
   cd scrapy_parser_pep
   ```

2. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
   pip install -r requirements.txt
   ```

---

## Запуск парсера

1. Запустите парсер:
   ```bash
   scrapy crawl pep
   ```

2. Результаты будут сохранены в директорию `results/`:
   - `pep_ДатаВремя.csv` — список всех PEP.
   - `status_summary_ДатаВремя.csv` — сводка по статусам PEP.

---

## Структура проекта

```
scrapy_parser_pep/
├── pep_parse/
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── pep.py
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── results/                  # Директория с результатами парсинга
├── tests/                    # Тесты
├── .flake8                   # Конфигурация Flake8
├── .gitignore                # Игнорируемые файлы
├── README.md                 # Этот файл
├── pytest.ini                # Конфигурация pytest
├── requirements.txt          # Зависимости
└── scrapy.cfg                # Конфигурация Scrapy
```

---

## Настройки

Основные настройки проекта находятся в файле `pep_parse/settings.py`:
- **FEEDS**: Настройки для сохранения результатов в CSV.
- **ITEM_PIPELINES**: Пайплайны для обработки данных.
- **DOWNLOAD_DELAY**: Задержка между запросами (по умолчанию 0.25 секунды).

---

## Тестирование

Для запуска тестов используйте команду:
```bash
pytest
```

---

## Результаты

### Пример файла `pep_ДатаВремя.csv`:
| number | name                          | status   |
|--------|-------------------------------|----------|
| 8      | PEP 8 – Style Guide for Python Code | Active   |
| 20     | PEP 20 – The Zen of Python     | Active   |
| ...    | ...                           | ...      |

### Пример файла `status_summary_ДатаВремя.csv`:
| Статус       | Количество |
|--------------|------------|
| Active       | 10         |
| Provisional  | 5          |
| Total        | 15         |

---

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

---

## Автор

- **Ваше имя**  
  - GitHub: [icek888]

---

Если у вас есть вопросы или предложения, пожалуйста, создайте issue или свяжитесь со мной. 😊
