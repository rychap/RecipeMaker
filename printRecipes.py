from IPython import embed
from Ingredient import *
from Measurement import *
from Recipe import *
from RecipeIngredient import *
from RecipesSerialization import * 
from Unit import *
from PGDatabaseConnector import *
from USDRParser import *
from PGDatabase import *

if __name__ == '__main__':
	database = PGDatabase()
	database.getAllRecipes()