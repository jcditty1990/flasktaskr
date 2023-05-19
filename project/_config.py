import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME =	'jcditty'
PASSWORD =	'jcditty1990'
WTF_CSRF_ENABLED = True
SECRET_KEY = '200263592'


# define the full path for the database

DATABASE_PATH = os.path.join(basedir, DATABASE)