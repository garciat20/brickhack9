from db.brickhack_db_utils import *

def setUp():
    build_tables()
    sample_data()
    # insert_data()

def build_tables():
    exec_sql_file('src/db/clothing_info.sql')

# def insert_data():
#     # insert from getData
#     return

def sample_data():
    return print(exec_get_all("SELECT * FROM buddy_table"))

def query(brands, types):
    sql = """
    SELECT * FROM """
    items = exec_get_all(sql)


