import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

SQLITE= {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

# 'db/sqlite/db.sqlite3'

POSTGRESQL= {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'db',
        'USER':'postgres',
        'PASSWORD':'193590Jaiguz',
        'HOST':'localhost',
        'PORT':'5432'
    }
}