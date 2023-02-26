from db.brickhack_db_utils import *

def setUp():
    build_tables()
    # sample_data()
    # insert_data()

def build_tables():
    exec_sql_file('src/db/clothing_info.sql')

# def insert_data():
#     # insert from getData
#     return

def get_all_items():
    # print(exec_get_all("SELECT * FROM buddy_table"))
    return exec_get_all("SELECT * FROM buddy_table")

def brand_and_category_items(name, category):
    return exec_get_all(f"""SELECT """)

def query(brands, types):
    sql = """
    SELECT * FROM """
    items = exec_get_all(sql)


