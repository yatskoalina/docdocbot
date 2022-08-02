import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [537487493]


ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv(('DATABASE')))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'