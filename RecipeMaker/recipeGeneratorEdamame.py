from IPython import embed
from Ingredient import *
from Measurement import *
from Recipe import *
from RecipeIngredient import *
from RecipesSerialization import * 
from Unit import *

APP_TOKEN = "b71bc2dc8ccfbfd51745fd85901226f9"
APP_ID = "8a80be6b"

def post(queryText, healthLabels="alcohol-free", maxNumIngredients=6, limit=10):
	import requests
	import json
	payload = {
			   	'q': queryText,
		  		'app_id': APP_ID,
		 		'app_key': APP_TOKEN,
		 		'from' : 0,
		 		'to': limit,
		 		"ingr": maxNumIngredients,
		 		# "health":healthLabels
		 		}	
	r = requests.post("https://api.edamam.com/search", params=payload)
	hits = json.loads(r.content)
	for hit in hits:
		recipe = hit["recipe"]
		ingredientList = []
		for ingredients in recipe["ingredients"]:
			for ingredient in ingredients:
				print ingredient
				# name, quantity = ingredient["text"]
				# ingredients.append(Ingredient())


if __name__ == '__main__':
	post("chicken")