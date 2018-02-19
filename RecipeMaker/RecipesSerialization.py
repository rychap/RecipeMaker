import json
from Ingredient import *
from Measurement import *
from Recipe import *
from RecipeIngredient import *
from RecipesSerialization import * 
from Unit import *

class RecipesSerialization():

	def deserializeRecipesFromFileNameJson(self, file_name):
		recipes = self.readJson(file_name)
		recipeList = []
		for recipe in recipes:
			recipe_ingredients = []
			ingredients = recipe["ingredients"]
			for ingredient_name, unit_string, amount in ingredients:
				unit = Unit.fromString(unit_string)
				ingredient = Ingredient(ingredient_name)
				measurement = Measurement(unit, amount)
				recipe_ingredient = RecipeIngredient(ingredient, measurement)
				recipe_ingredients.append(recipe_ingredient)
			recipe = Recipe(recipe["name"], recipe["num_servings"], recipe_ingredients, recipe["cuisine"], recipe["meal_type"])
			recipeList.append(recipe)
		return recipeList
		
	def serializeRecipesObjectToFile(file_name, recipesList):
		recipesJson = []
		for recipe in recipesList:
			# TODO
			pass
		writeJson(file_name, recipeJson)

	def writeJson(self, file_name, data):
		with open(file_name, 'w') as outfile:
		    json.dump(data, outfile)

	def readJson(self, file_name):
		with open(file_name) as json_file:  
		    data = json.load(json_file)
		    return data