from IPython import embed
from Ingredient import *
from Measurement import *
from Recipe import *
from RecipeIngredient import *
from RecipesSerialization import * 
from Unit import *
from DatabaseManager import *
from USDRParser import *
from PGDatabase import *

if __name__ == '__main__':
	# PGDatabase().dropTables()
	# PGDatabase().create_all_tables()
	# data = USDRParser().readFoodDescription()
	# PGDatabase().insertFoodDescriptions(data)
	results = DatabaseManager().fetchIngredientsFromSearch("milk", 10)
	print(results)

