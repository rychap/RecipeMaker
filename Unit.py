from Exceptions import *
from enum import Enum

class Unit(Enum):
	# Volume
	GALLON = "gallon"
	QUART = "quart"
	PINT = "pint"
	CUP = "cup"
	FLOZ = "fluid_ounce"
	TBSP = "tablespoon"
	TSP = "teaspoon"

	# Mass
	LB = "pound"
	OZ = "ounce"
	GRAM = "gram"
	KGRAM = 'kilo_gram'

	@classmethod
	def fromString(cls, unit_string):
		if (unit_string == "gallon"):
			return cls.GALLON
		if (unit_string == "quart"):
			return cls.QUART
		if (unit_string == "pint"):
			return cls.PINT
		if (unit_string == "cup"):
			return cls.CUP
		if (unit_string == "fluid_ounce"):
			return cls.FLOZ
		if (unit_string == "tablespoon"):
			return cls.TBSP
		if (unit_string == "teaspoon"):
			return cls.TSP
		if (unit_string == "pound"):
			return cls.LB
		if (unit_string == "ounce"):
			return cls.OZ
		if (unit_string == "gram"):
			return cls.GRAM
		if (unit_string == "kilo_gram"):
			return cls.KGRAM
		raise InvalidUnit("Invalid unit: %s" % unit_string)
