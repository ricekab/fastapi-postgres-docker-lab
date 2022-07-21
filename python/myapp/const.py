import os

DB_URL_DEFAULT = 'postgresql+psycopg2://fastapidbo:fastapidevelopment@db/appdb'
DB_URL = os.environ.get('MYAPP_DB_URL', DB_URL_DEFAULT)
