import requests
import json
import logging
import time
import threading

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)

def main(url):
    while 1:
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = json.loads(r.content)
            logging.info("Сервер доступний. Час на сервері: %s", data['date'])
            logging.info("Запитувана сторінка: : %s", data['current_page'])
            logging.info("Відповідь сервера місти наступні поля:")
            for key in data.keys():
                logging.info("Ключ: %s, Значення: %s", key, data[key])
        except Exception as e:
            logging.error("Exception: %s", e)
        time.sleep(60)


if __name__ == '__main__':
    main("http://localhost:8000/health")