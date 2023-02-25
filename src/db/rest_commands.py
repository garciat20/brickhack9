from db.brickhack_db_utils import *

def setUp():
    build_tables()
    # insert_data()

def build_tables():
    exec_sql_file('src/db/clothing_info.sql')

# def insert_data():
#     # insert from getData
#     return


def query(brands, types):
    sql = """
    SELECT * FROM """
    items = exec_get_all(sql)


