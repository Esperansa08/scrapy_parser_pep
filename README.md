# Асинхронный парсер PEP

Проект асинхронного парсера позволяет получать список всех PEP для Python и информацию по статусам и количеству PEP,

с записью полученной информации в файлы. на базе фреймворка Scrapy.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)

## Описание

Собирает номер, название и статус всех PEP.

Парсер собирает данные с сайта https://www.python.org/

Подсчитывает общее количество каждого статуса, а также общую сумму всех статусов.

Вся собранная информация сохраняется в файлах формата .csv в папке "results/" с указанием даты и времени парсинга.

pep_(data).csv :: номер PEP, название и статус
status_summary_(data).csv :: статистика PEP по статусам и сумма документов PEP

### Используемые технологии:
+ Python
+ Scrapy


## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Esperansa08/scrapy_parser_pep.git
```

Создать и активировать виртуальное окружение:
```
python -m venv venv
```

```
venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

## Запуск парсера

Парсер запускается из root-директории проекта командой
```
scrapy crawl pep
```

### Автор 

 * Савельева Анастасия (Visteria09@yandex.ru, https://github.com/Esperansa08) 