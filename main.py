import time

import fdb
import schedule
import requests
from src.devino import send
from src.config import MIKE_NUMBER, GLEB_NUMBER, SERG_NUMBER, STOCK_ACCESS_TOKEN, COMPANY_ACCESS_TOKEN, \
    AGENT_ACCESS_TOKEN, DB_HOST, DB_PORT, \
    DB_DATABASE, DB_USER, DB_PASSWORD, TEST_NUMBER

NUMBERS = [MIKE_NUMBER, GLEB_NUMBER, SERG_NUMBER]


def check_backend():
    response = requests.get('https://back.artlife.ru/stocks/stock_profile',
                            headers={'access-token': STOCK_ACCESS_TOKEN},
                            verify=False)
    if response.status_code != 200:
        message = 'Бэкенд упал'
        for number in NUMBERS:
            send(number, message)


def check_database():
    try:
        fdb.connect(host=DB_HOST,
                    port=int(DB_PORT),
                    database=DB_DATABASE,
                    user=DB_USER,
                    password=DB_PASSWORD)
    except:
        message = 'БД упала'
        for number in NUMBERS:
            send(number, message)


def check_stock_frontend():
    response = requests.get('https://store.artlife.ru/',
                            headers={'access-token': STOCK_ACCESS_TOKEN},
                            verify=False)
    if response.status_code != 200:
        message = 'Фронтенд ЛК Склада упал'
        for number in NUMBERS:
            send(number, message)


def check_partner_frontend():
    response = requests.get('https://partner.artlife.ru/',
                            headers={'access-token': AGENT_ACCESS_TOKEN},
                            verify=False)
    if response.status_code != 200:
        message = 'Фронтенд ЛК Партнера упал'
        for number in NUMBERS:
            send(number, message)


def check_company_frontend():
    response = requests.get('https://company.artlife.ru/',
                            headers={'access-token': COMPANY_ACCESS_TOKEN},
                            verify=False)
    if response.status_code != 200:
        message = 'Фронтенд ЛК Компании упал'
        for number in NUMBERS:
            send(number, message)


if __name__ == '__main__':
    schedule.every(10).minutes.do(check_database)
    schedule.every(10).minutes.do(check_backend)
    schedule.every(10).minutes.do(check_stock_frontend)
    schedule.every(10).minutes.do(check_company_frontend)
    schedule.every(10).minutes.do(check_partner_frontend)

    while True:
        schedule.run_pending()
        time.sleep(1)
