import os
from dotenv import load_dotenv

load_dotenv()

TABLENAME = os.environ.get('TABLENAME', 'HSsum')
TESTUSER = os.environ.get('TESTUSER', 'testuser')

