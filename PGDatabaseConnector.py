from Interface import implements
from PGDatabase import *
from DatabaseInterface import *
from Recipe import *

class PGDatabaseConnector(implements(DatabaseInterface)):

	def fetchIngredientsFromSearch(self, term, limit):
		results = PGDatabase().getIngredientsFromSearchTerm(term, limit)
		return results

	def createRecipe(self, recipe):
		if not recipe.name:
			raise MissingRecipeField("Missing name")
		if not recipe.servingSize:
			raise MissingRecipeField("Missing serving size")
		if not recipe.cuisine:
			raise MissingRecipeField("Missing cuisine")
		if not recipe.mealType:
			raise MissingRecipeField("Missing meal type")
		if not recipe.ingredients:
			raise MissingRecipeField("Missing ingredients")

		PGDatabase().insertRecipe(recipe.name, recipe.servingSize, recipe.cuisine, recipe.mealType, recipe.ingredients)