from db.brickhack_db_utils import *
BRANDS = ["kappa"]
BRANDS_WEB_SCRAPPED = ["src/db/kappa_get_data.py"]

# def setUp():
#     build_tables()
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

def get_brand_and_category_items(name, category):
    return exec_get_all(f"""SELECT """)

def get_brand_items(name):
    name = name.lower()
    if name in BRANDS:
        for file in BRANDS_WEB_SCRAPPED:
            #result = kappa_get_data --> result[0] --> kappa
            if name.lower() == file.split('_',1)[0]:
                # load specific brand data into tables
                exec(file)
    else:
        return
    # sql file made, now load into db
    # build_tables()
    return exec_get_all(f"SELECT * FROM buddy_table")

def query(brands, types):
    sql = """
    SELECT * FROM """
    items = exec_get_all(sql)


