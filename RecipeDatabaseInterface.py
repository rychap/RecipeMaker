from interface import Interface

class RecipeDatabaseInterface(Interface):

    def fetchAllRecipes(self):
        pass

    def fetchRecipesWithSimilarIngredients(self, ingredientIDs, limit):
        pass