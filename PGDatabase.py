#!/usr/bin/python
import psycopg2
from config import config
 
class PGDatabase(object):
    def __init__(self):
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        self._db_conn = psycopg2.connect(**params)
        self._db_cur = self._db_conn.cursor()

    def create_food_des_tables(self):
        command = """CREATE TABLE usda_food_des (
                            nut_db_id INTEGER NOT NULL,
                            food_grp_code INTEGER NOT NULL,
                            long_desc VARCHAR(200) NOT NULL,
                            short_desc VARCHAR(60) NOT NULL,
                            common_name VARCHAR(100),
                            manufac_name VARCHAR(65),
                            survey CHAR,
                            ref_desc VARCHAR(135),
                            refuse INTEGER,
                            sci_name VARCHAR(65),
                            n_factor DECIMAL(4,2),
                            pro_factor DECIMAL(4,2),
                            fat_factor DECIMAL(4,2),
                            cho_factor DECIMAL(4,2)
                        )"""
        self._db_cur.execute(command)
        self._db_conn.commit()

    def create_recipe_tables(self):
        command = """CREATE TABLE usda_food_des (
                            
                        )"""
        self._db_cur.execute(command)
        self._db_conn.commit()

    def insertFoodDescriptions(self, food_dicts):
        """ insert a new vendor into the vendors table """
        for food_dict in food_dicts:
            placeholders = ', '.join(['%s'] * len(food_dict))
            columns = ', '.join(food_dict.keys())
            sql = "INSERT INTO usda_food_des( %s ) VALUES ( %s ) RETURNING nut_db_id" % (columns, placeholders)
            self._db_cur.execute(sql, food_dict.values())
            nut_db_id = self._db_cur.fetchone()[0]

        self._db_conn.commit()        

    def getAllFoodDescriptions(self):
        """ insert a new vendor into the vendors table """
        sql = "SELECT * from usda_food_des"
        self._db_cur.execute(sql)

        row = self._db_cur.fetchone()
 
        while row is not None:
            print(row)
            row = self._db_cur.fetchone()

    def getIngredientsFromSearchTerm(self, term, limit):
        """ insert a new vendor into the vendors table """
        sql = "SELECT long_desc FROM usda_food_des WHERE position('%s' in LOWER(long_desc)) > 0 LIMIT %d" % (term, limit)
        self._db_cur.execute(sql)

        row = self._db_cur.fetchone()
 
        while row is not None:
            print(row)
            row = self._db_cur.fetchone()

    def __del__(self):
        self._db_conn.close()

