import os
import fdb
from dotenv import load_dotenv
load_dotenv()

DEVINO_API_KEY = os.environ.get('DEVINO_API_KEY')
GLEB_NUMBER = os.environ.get('GLEB_NUMBER')
MIKE_NUMBER = os.environ.get('MIKE_NUMBER')
SERG_NUMBER = os.environ.get('SERG_NUMBER')
TEST_NUMBER = os.environ.get('TEST_NUMBER')

STOCK_ACCESS_TOKEN = os.environ.get('STOCK_ACCESS_TOKEN')
COMPANY_ACCESS_TOKEN = os.environ.get('COMPANY_ACCESS_TOKEN')
AGENT_ACCESS_TOKEN = os.environ.get('AGENT_ACCESS_TOKEN')

DB_HOST = os.environ.get('DB_HOST')
DB_DATABASE = os.environ.get('DB_DATABASE')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')


