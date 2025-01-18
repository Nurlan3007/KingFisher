<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>О проекте</h1>
  <p>
    Это тестовое задание для дуального обучения студента Марата Нурлана Бда-2302.
    Задача - парсер для получения данных с сайта <a href="https://kingfisher.kz/" target="_blank">Kingfisher.kz</a>.
  </p>
  <h1>Структура проекта</h1>
  <p>Проект имеет следующую структуру:</p>
  <pre>
  /project-root
  │
  ├── /postgres                # Папка с конфигурацией для базы данных (docker-compose.yml)
  │   └── docker-compose.yml   # Конфигурация для поднятия контейнера PostgreSQL
  │   └── sqlCode.sql          # SQL скрипт для создания структуры базы данных
  │
  ├── /parser                  # Папка с файлами парсера
  │   ├── parserForCategoryInsertDb.py   # Парсер для извлечения категорий и подкатегорий
  │   └── parserForProducts.py          # Парсер для извлечения данных товаров
  │
  ├── /analysis                # Папка с анализом данных
  │   ├── top_10Price.py       # Скрипт для построения графика с ценами
  │   └── count_vs_price.py    # Скрипт для построения графика рассеяния
  │
  └── README.md               # Этот файл
    </pre>
  <p>
    <b>Цель проекта:</b>
    <ol>
      <li>Парсинг данных с сайта: извлечение информации о товарах с сайта Kingfisher.kz.</li>
      <li>Хранение данных в PostgreSQL: создание базы данных и таблиц для хранения информации.</li>
      <li>Визуализация данных: построение графиков и диаграмм для анализа цен, рейтингов и других характеристик товаров.</li>
    </ol>
  </p>

  <h1>Технологии</h1>
  <p>
    <b>Основные технологии:</b>
    <ul>
      <li>PostgreSQL</li>
      <li>Python</li>
      <li>Visual Studio Code</li>
    </ul>
    <b>Python-модули:</b>
    <ul>
      <li>BeautifulSoup4</li>
      <li>Requests</li>
      <li>psycopg2 (для подключения к PostgreSQL)</li>
      <li>Pandas</li>
      <li>Matplotlib</li>
    </ul>
  </p>

  <h1>Необходимые библиотеки</h1>
  <p>
    Установите все зависимости с помощью pip:
  </p>
  <pre>
pip install psycopg2 pandas matplotlib beautifulsoup4 lxml requests
  </pre>

  <h1>How to Start the Parser</h1>
  <h3>Шаг 1: Подключение к базе данных</h3>
  <p>
    Сначала нужно подключиться к базе данных. В папке <code>postgres</code> находится файл <code>docker-compose.yml</code>. 
    Запустите команду:
  </p>
  <pre>
docker compose up
  </pre>
  <p>
    Параметры базы данных:
    <ul>
      <li><b>Пароль:</b> 12345</li>
      <li><b>Имя базы данных:</b> king_fisher1</li>
      <li><b>Пользователь:</b> postgres</li>
      <li><b>Порт:</b> 5438:5432</li>
    </ul>
    После запуска подключитесь к базе данных и вставьте SQL-код из файла <code>sqlCode.sql</code>.
  </p>

  <h3>Шаг 2: Получение данных</h3>
  <p>
    Чтобы получить данные с сайта:
    <ol>
      <li>Запустите файл <code>parserForCategoryInsertDb.py</code> из папки <code>парсер</code>.</li>
      <li>Затем запустите файл <code>parserForProducts.py</code> из той же папки. Данные будут добавлены в базу данных.</li>
    </ol>
    <b>Как работает парсер:</b>
    <ol>
      <li>Сначала извлекаются все категории и подкатегории с их ссылками, затем они добавляются в базу данных (файл <code>parserForCategoryInsertDb.py</code>).</li>
      <li>Из базы данных берутся подкатегории и их ссылки. Эти ссылки объединяются с основным адресом <a href="https://kingfisher.kz/" target="_blank">https://kingfisher.kz/</a> с помощью конкатенации. После этого парсер переходит по каждой странице подкатегории, например: "Морепродукты креветки" будет преобразовано в <code>https://kingfisher.kz/moreprodukty/krevetki/</code> (файл <code>parserForProducts.py</code>).</li>
    </ol>
  </p>

  <h1>Анализ</h1>
  <p>
    Визуализация данных выполняется с помощью библиотеки Matplotlib для построения графиков и анализа. В папке <code>analysis</code> находятся два файла:
    <ul>
      <li><b>top_10Price.py</b> — в этом файле получаем из базы данных сумму всех цен и количество товаров в каждой подкатегории и строим горизонтальный столбчатый график</li>
      <li><b>count_vs_price.py</b> — строится график типа scatter для визуализации того, что большое количество товаров в подкатегории не всегда означает, что эта подкатегория будет самой дорогой.</li>
      <li><b>top10_products.py</b> — строю горизонтальный столбчатый график топ 15 самых дорогих товаров </li>
    </ul>
  </p>
</body>
</html>
