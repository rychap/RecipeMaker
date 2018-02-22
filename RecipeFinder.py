from Ingredient import *
from Measurement import *
from Recipe import *
from RecipeDatabaseInterface import *
from RecipeDatabaseManager import *
from RecipeIngredient import *
from RecipeIngredientList import *
from RecipesSerialization import * 
from Unit import *

class RecipesFinder():

	# Given an array of recipes, generate the recipe that most likely fits with the provided recipes
	def findRecipesWithSimilarIngredients(recipes, limit):
		ingredientList = RecipeIngredientList(recipes)
		# Get recipe ids from all of the recipes 
		ingredientIDs = ingredientList.getIngredientIDs()
		# Find recipes with relevant ingredients 
		recipeDatabaseManager = RecipeDatabaseManager()

		results = recipeDatabaseManager.fetchRecipesWithSimilarIngredients(ingredientIDs, limit)

		return results

	# Given an array of recipes, generate the recipe that most likely fits with the provided recipes within the cuisine
	def findRecipeWithSimilarIngredientsForCuisine(recipes, limit, cuisine):

		return 0
