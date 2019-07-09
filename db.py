from sqlalchemy import create_engine
from string import Template
from sqlalchemy.orm import sessionmaker

DB = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'pwd': 'YourPassword',
    'db_name': 'nutt'
}


def get_engine():
    conn_str_template = 'mysql+pymysql://$user:$pwd@$host:$port/$db_name?connect_timeout=6000'
    conn_str = Template(conn_str_template).substitute(DB)
    engine = create_engine(conn_str)
    return engine


def get_session():
    engine = get_engine()
    db_session = sessionmaker(bind=engine)
    return engine, db_session()
