# Lab 3
1. Створив папку *Lab 3*. Перейшов у папку та ініцілізував середовище `pipenv` та встановив пакети `django`.
2. За допомогою Django Framework створив заготовку проекту з назвою *my_site*.
3. Запустив Django сервер.
![Django server](https://github.com/GamTdz/devLabs/blob/master/lab3/img/Django_sever.png "Django server")
4. Створив темплейт додатку та назвав його *main*.
5. За допомогою IntelliJ створив `main/templates/main.html` та `main/urls.py`.
6. Створив дві сторінки *main* і *health*.
![main](https://github.com/GamTdz/devLabs/blob/master/lab3/img/main.png "main")
7. Перевірив, що сторінка *health* відображається.
![health](https://github.com/GamTdz/devLabs/blob/master/lab3/img/health.png "health")
8. Встановив бібліотеку `requests` для моніторингу.
9. Модифікував функцію `health` так щоб у відповіді були згенеровані дата, URL сторінки моніторингу, інформація про сервер на якому запущений сайт та інформація про клієнта який робить запит до сервера.
![modifiedHealth](https://github.com/GamTdz/devLabs/blob/master/lab3/img/modifiedHealth.png "modifiedHealth")
10. Дописав функціонал який буде виводити повідомлення про недоступність сторінки.
11. Моніторинг запускається раз в хвилину.
12. Добавив аліас на запуск сервера, та моніторингу.
13. Зробив зміни в файлі `README.md`, та закомітив зміни.