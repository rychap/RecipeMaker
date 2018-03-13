from PGDatabaseConnector import *
from USDRParser import *
from PGDatabase import *


if __name__ == '__main__':

	PGDatabase().create_all_tables()
	data = USDRParser().readFoodDescription()
	PGDatabase().insertFoodDescriptions(data)