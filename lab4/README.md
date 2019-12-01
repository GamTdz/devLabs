# Lab 4
1. Для перевірки чи докер працює ввів наступні команди, та перенаправив результат їхнього виконання у файл `my_work.log`:
```
docker -v
docker -h
docker run docker/whalesay cowsay Docker is fun
```
2. Завантажив базовий імейдж репозиторію використовуючи наступні команди:
```
docker pull python:3.7-slim
docker images
docker inspect python:3.7-slim
```
3. Створив свій файл Dockerfile.
4. Створив власний репозиторій на Docker Hub також виконав та завантажив білд:
```
docker build -t gamtdz/lab4:django .
docker images
docker push gamtdz/lab4:django
```
[Посилання на Docker Hub](https://hub.docker.com/repository/docker/gamtdz/lab4/general)
5. Запустив веб-сайт наступною командою:
```
docker run -it --name=django --rm -p 8000:8000 gamtdz/lab4:django
```
![Docker run](https://github.com/GamTdz/devLabs/blob/master/lab4/img/dockerRun.png "dockerRun")
6. Створив ще один контейнер з програмою моніторингу нашого веб-сайту за допомогою файлу `Dockerfile.monitoring`.
7. Виконав білд та запустив одночасно веб-сайт та моніторинг (щоб уникнути проблем з мережею використав ключ `--net=host`).
8. Закомітив файли.
