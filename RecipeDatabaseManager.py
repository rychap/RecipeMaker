from interface import implements

class RecipeDatabaseManager(implements(RecipeDatabaseInterface)):

	def fetchAllRecipes(self):
        return []

    def fetchRecipesWithSimilarIngredients(self, ingredientIDs, limit):
        return []