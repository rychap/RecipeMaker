#!/usr/bin/python
import psycopg2
from config import config
from Ingredient import *
from RecipeIngredient import *
 
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
        self.create_join_recipe_ingredient_table()

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

    def create_join_recipe_ingredient_table(self):
        command = """CREATE TABLE IF NOT EXISTS join_recipe_ingredient (
                            recipe_id INTEGER,
                            ingredient_id INTEGER,
                            quantity DECIMAL(4,2),
                            unit VARCHAR(60),
                            FOREIGN KEY (recipe_id) REFERENCES  recipes(id),
                            FOREIGN KEY (ingredient_id) REFERENCES  usda_food_des(id),
                            CONSTRAINT join_id PRIMARY KEY (recipe_id, ingredient_id)
                        )"""
        self._db_cur.execute(command)
        print("join_recipe_ingredient table created.")
        self._db_conn.commit()

    def dropTables(self):
        commands = (
            "DROP TABLE usda_food_des cascade",
            "DROP TABLE recipes cascade",
            "DROP TABLE join_recipe_ingredient cascade"
        )
        for command in commands:
            self._db_cur.execute(command)
            print("Tables deleted")
        self._db_conn.commit()


    def insertFoodDescriptions(self, food_dicts):
        for food_dict in food_dicts:
            placeholders = ', '.join(['%s'] * len(food_dict))
            columns = ', '.join(food_dict.keys())
            sql = "INSERT INTO usda_food_des( %s ) VALUES ( %s ) RETURNING id" % (columns, placeholders)
            self._db_cur.execute(sql, food_dict.values())
            nut_db_id = self._db_cur.fetchone()[0]

        self._db_conn.commit()

    def insertRecipe(self, name, serving_size, cuisine, mealType, ingredients):

        sql = "INSERT INTO recipes (name, serving_size, cuisine, meal_type) VALUES ('%s',%d,'%s','%s') RETURNING id" % (name, serving_size, cuisine, mealType)

        self._db_cur.execute(sql, (name, serving_size, cuisine, mealType))
        recipeID = self._db_cur.fetchone()[0]

        for ingr in ingredients:
            values = (recipeID, ingr.ingredient.id, ingr.measurement.quantity, ingr.measurement.unit)
            for val in values:
                if not val:
                    raise MissingRecipeField("Missing ingredient field for recipe insertion.")
            sql = "INSERT INTO join_recipe_ingredient(recipe_id,ingredient_id,quantity,unit) VALUES (%s,%s,%d,'%s')" % (recipeID, ingr.ingredient.id, ingr.measurement.quantity, ingr.measurement.unit)
            self._db_cur.execute(sql, (recipeID, ingr.ingredient.id, ingr.measurement.quantity, ingr.measurement.unit))

        self._db_conn.commit()  

    def getAllFoodDescriptions(self):
        """ insert a new vendor into the vendors table """
        sql = "SELECT * from usda_food_des"
        self._db_cur.execute(sql)

        row = self._db_cur.fetchone()

        results = [row]
 
        while row is not None:
            row = self._db_cur.fetchone()
            results.append(row)

        return results

    def getAllJoins(self):
        """ insert a new vendor into the vendors table """
        sql = "SELECT * from join_recipe_ingredient"
        self._db_cur.execute(sql)

        row = self._db_cur.fetchone()

        results = [row]
 
        while row is not None:
            print(row)
            row = self._db_cur.fetchone()
            results.append(row)

        return results

    def getIngredientsFromSearchTerm(self, term, limit):
        """ insert a new vendor into the vendors table """
        sql = "SELECT * FROM usda_food_des WHERE position('%s' in LOWER(long_desc)) > 0 LIMIT %d" % (term, limit)
        self._db_cur.execute(sql)

        results = []
        row = self._db_cur.fetchone()
 
        while row is not None:
            ingr = Ingredient(row[0], row[3])
            results.append(ingr)
            row = self._db_cur.fetchone()

        return results

    def __del__(self):
        self._db_conn.close()

