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
	databaseConnector = PGDatabaseConnector()

	ingredients = databaseConnector.fetchIngredientsFromSearch("cheese", 10)

	ris = []

	for ingr in ingredients:
		if not ingr:
			continue
		ri = RecipeIngredient(None, ingr, Measurement('cup', 2.0))
		ris.append(ri)

	recipe = Recipe(None, "Cheese soufle", 4, ris, "italian", "dinner")

	databaseConnector.createRecipe(recipe)

