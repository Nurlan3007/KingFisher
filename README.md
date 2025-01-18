
<h1>---About the Project</h1>
<p>
  Это тестовое задание для дуального обучения студента Марата Нурлана Бда-2302.
  Задача - парсер для получения данных с сайта https://kingfisher.kz/.

  Цель Проект 
  1. Парсинг данных с сайта: извлечение информации о товарах с сайта Kingfisher.kz.
  2. Хранение данных в PostgreSQL: создание базы данных и таблиц для хранения информации.
  3. Визуализация данных: построение графиков и диаграмм для анализа цен, рейтингов и других характеристик товаров.
</p>
<h1>Технологии</h1>
<p>
  <ul>
    <li>Postgresql</li>
    <li>Python</li>
    <li>Visual Studio Code</li>
  </ul>
  <ul><b>Modules Python</b>
     <li>BeautifulSoup4</li>
     <li>Requests</li>
     <li>psycopg2, for connect to PostgreSql</li>
     <li>Pandas</li>
  </ul>
</p>
<h1>Необходимые библиотеки с помощью pip</h1>
<p>
  pip install psycopg2 pandas matplotlib beautifulsoup4 lxml requests
</p>

<h1>Как запустить парсер</h1>
<p>
   <h3>Шаг 1</h3>
   <p>
     Сначала нужно подключиться к базе дданных в папке postgres есть docker-compose.yml, 
     запускаем команду <br>
	`docker compose up`
	<ul>
		<li>password db = 12345</li>
		<li>db name = king_fisher1</li>
		<li>db user = postgres</li>
		<li>db port = 5438:5432</li>
     </ul>
     подключаемся и вставляем sql code из sqlCode.sql
   </p>
   <h3>Шаг 2</h3>
   <p>
      Чтобы получить данные из сайты,
      Gервое надо запустить файл parserForCategoryInsertDb.py в папке парсер
      Второе запускаем файл parserForProducts.py в папке парсер и данные появится в базе данных
	   <br>
      <h5>Как работает парсер</h5> <br>
      1. Сначала я получаю все категории и подкатегории и их ссылки и добавляю в ДБ (файл parserForCategoryInsertDb.py) <br>
      2. Потом я достаю все подкатегории и ссылки из БД обьелиняю с главное ссылкой https://kingfisher.kz/ при помощи конкатенации и достаю каждую страницы подкатегории например "Морепродукты креветки" https://kingfisher.kz/moreprodukty/ + krevetki/ (Файл parserForProducts.py)
     		
   </p>
</p>
<h1>Анализ</h1>
<p></p>




