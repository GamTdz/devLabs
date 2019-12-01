# Lab 5
1. Створив папку `my-app`, `tests` та скопіював файли з вашого репозиторію.
2. Використовуючи наступні команди спробував, чи проект і тести є працездатними:
```
pipenv --python 3.7
pipenv install -r requirenets.txt
pipenv run python app.py
pipenv run pytest test_app.py --url http://localhost:5000
```
3. ![failedTests](https://github.com/GamTdz/devLabs/blob/master/lab5/img/failedTests.png "failedTests")
4. Видалив всі файли, що створились.
5. Ознайомився зі вмістом Dockerfile та Makefile.
...STATES       - ім'я тегу
...REPO         - назва репозиторію
...run          - запуск сайту
...test-app     - запуск тестів
...docker-prune - чистка ресурсів Docker
6. Використовуючи команду `make` створив Docker імеджі для додатку та для тестів.
7. Переконався, що тести пройшли успішно.
8. ![passedTests](https://github.com/GamTdz/devLabs/blob/master/lab5/img/passedTests.png "passedTests")
9. Переконався, що сайт працює успішно. `main`:
10. ![main](https://github.com/GamTdz/devLabs/blob/master/lab5/img/main.png "main")
11. ![pageHits](https://github.com/GamTdz/devLabs/blob/master/lab5/img/pageHits.png "pageHits")
12. ![pageLogs](https://github.com/GamTdz/devLabs/blob/master/lab5/img/pageLogs.png "pageLogs")
13. Перевірив, що Docker-compose встановлений та працює у моїй системі за допомогою команд:
```
docker-compose version
docker-compose -p lab5 up
```
14. ![dockerCompose](https://github.com/GamTdz/devLabs/blob/master/lab5/img/dockerCompose.png "dockerCompose")
15. Перевірив, чи працює веб-сайт:
16. ![dockerComposeWeb](https://github.com/GamTdz/devLabs/blob/master/lab5/img/dockerComposeWeb.png "dockerComposeWeb")
17. Перевірив, чи компоуз створив докер імеджі:
18. ![dockerComposeImages](https://github.com/GamTdz/devLabs/blob/master/lab5/img/dockerComposeImages.png "dockerComposeImages")
19. Завантажив створені імеджі до Docker Hub репозиторію за допомогою команди:
```
docker-compose push
```
20. Для лабораторної роботи №4 створив свій docker-compose.yaml.
21. Створив два імеджі для Django сайту та моніторингу, та успішно їх запустив.
22. ![ComposeDjangoConsole](https://github.com/GamTdz/devLabs/blob/master/lab5/img/composeDjangoConsole.png "ComposeDjangoConsole")
23. ![ComposeAppWork](https://github.com/GamTdz/devLabs/blob/master/lab5/img/composeAppWork.png "ComposeAppWork")
24. ![ComposeHealth](https://github.com/GamTdz/devLabs/blob/master/lab5/img/composeHealth.png "ComposeHealth")
25. Завантажив імеджі на [Docker Hub](https://hub.docker.com/repository/docker/gamtdz/lab4)