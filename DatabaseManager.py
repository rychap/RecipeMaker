from Interface import implements
from PGDatabase import *
from DatabaseInterface import *

class DatabaseManager(implements(DatabaseInterface)):

	def fetchIngredientsFromSearch(self, term, limit):
		results = PGDatabase().getIngredientsFromSearchTerm(term, limit)
		return results