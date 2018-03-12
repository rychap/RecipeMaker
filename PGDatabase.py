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

    def create_all_tables(self):
        self.create_recipe_table()
        self.create_food_des_table()
        self.create_ingredient_list_table()

    def create_food_des_table(self):
        command = """CREATE TABLE IF NOT EXISTS usda_food_des (
                            id SERIAL PRIMARY KEY,
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
        print("usda_food_des table created.")
        self._db_conn.commit()

    def create_recipe_table(self):
        command = """CREATE TABLE IF NOT EXISTS recipes (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(60) NOT NULL,
                            serving_size INTEGER,
                            cuisine VARCHAR(60),
                            meal_type VARCHAR(60)
                        )"""
        self._db_cur.execute(command)
        print("recipes table created.")
        self._db_conn.commit()

    def create_ingredient_list_table(self):
        command = """CREATE TABLE IF NOT EXISTS join_recipe_ingredient (
                            recipe_id INTEGER NOT NULL,
                            ingredient_id INTEGER NOT NULL,
                            quantity DECIMAL(4,2),
                            unit VARCHAR(60), 
                            PRIMARY KEY (recipe_id,ingredient_id)
                        )"""
        self._db_cur.execute(command)
        print("join_recipe_ingredient table created.")
        self._db_conn.commit()

    def dropTables(self):
        commands = (
            "DROP TABLE usda_food_des",
            "DROP TABLE recipes",
            "DROP TABLE join_recipe_ingredient"
        )
        for command in commands:
            self._db_cur.execute(command)
            print("Tables deleted")
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
        sql = "SELECT * FROM usda_food_des WHERE position('%s' in LOWER(long_desc)) > 0 LIMIT %d" % (term, limit)
        self._db_cur.execute(sql)

        row = self._db_cur.fetchone()
 
        while row is not None:
            print(row)
            row = self._db_cur.fetchone()

    def __del__(self):
        self._db_conn.close()

