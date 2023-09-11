import time

import fdb
import schedule
import requests
from src.devino import send
from src.config import MIKE_NUMBER, GLEB_NUMBER, SERG_NUMBER, STOCK_ACCESS_TOKEN, COMPANY_ACCESS_TOKEN, AGENT_ACCESS_TOKEN, DB_HOST, DB_PORT, \
    DB_DATABASE, DB_USER, DB_PASSWORD

numbers = [MIKE_NUMBER, GLEB_NUMBER, SERG_NUMBER]


def check_stocks_backend():
    response = requests.get('https://back.artlife.ru/stocks/stock_profile',
                            headers={'access-token': STOCK_ACCESS_TOKEN},
                            verify=False)
    if response.status_code != 200:
        message = 'ЛК Склада упал'
        for number in numbers:
            send(number, message)


def check_partner_backend():
    response = requests.get('https://back.artlife.ru/agent/profile',
                            headers={'access-token': AGENT_ACCESS_TOKEN},
                            verify=False)
    if response.status_code != 200:
        message = 'ЛК Партнера упал'
        for number in numbers:
            send(number, message)


def check_company_backend():
    response = requests.get('https://back.artlife.ru/company/price-list/1',
                            headers={'access-token': COMPANY_ACCESS_TOKEN},
                            verify=False)
    if response.status_code != 200:
        message = 'ЛК Компании упал'
        for number in numbers:
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
        for number in numbers:
            send(number, message)


if __name__ == '__main__':
    schedule.every(10).minutes.do(check_database)
    schedule.every(10).minutes.do(check_stocks_backend)
    schedule.every(10).minutes.do(check_company_backend)
    schedule.every(10).minutes.do(check_partner_backend)

    while True:
        schedule.run_pending()
        time.sleep(1)
