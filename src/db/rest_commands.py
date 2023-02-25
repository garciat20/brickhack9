from brickhack_db_utils import *
from getData import *

def setUp():
    build_tables()
    insert_data()

def build_tables():
    exec_sql_file("schema.sql")
    return

def insert_data():
    # insert from getData
    return


def query(brands, types):
    sql = """
    SELECT * FROM """
    items = exec_get_all(sql)


