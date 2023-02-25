from .brickhack_db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/clothing_info.sql')
