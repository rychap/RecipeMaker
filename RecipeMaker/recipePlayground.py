from IPython import embed
from Ingredient import *
from Measurement import *
from Recipe import *
from RecipeIngredient import *
from RecipesSerialization import * 
from Unit import *

if __name__ == '__main__':
	recipesJson = 	[
					{
						"name": "dank_chicken",
						"ingredients": [
											("chicken", "pound", 0.5),
											("mushroom", "ounce", 4)
										],
						"cuisine": "American",
						"meal_type": "dinner",
						"num_servings": 10
					}
				]
	serializer = RecipesSerialization()
	serializer.writeJson("recipes-test.json", recipesJson)

	recipes = serializer.deserializeRecipesFromFileNameJson("recipes-test.json")


