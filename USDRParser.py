import re

class USDRParser():

	def readFoodDescription(self):
		des_headers = [
			"nut_db_id",
			"food_grp_code",
			"long_desc",
			"short_desc",
			"common_name",
			"manufac_name",
			"survey",
			"ref_desc",
			"refuse",
			"sci_name",
			"n_factor",
			"pro_factor",
			"fat_factor",
			"cho_factor"
		]
		foodObjs = self.readSRFile("data/FOOD_DES.txt", des_headers)
		return foodObjs

	def readSRFile(self, fname, hdrs):
		result = []
		with open(fname, "r") as ins:
		    for line in ins:
		        item = self.parseLine(line.strip(), hdrs)
		    	result.append(item)
		return result

	def parseLine(self, line, hdrs):
		values = line.split('^')
		foodItem = {}
		for i in range(0,len(values)):
			pVal = values[i]
			key = hdrs[i]
			m = re.search('~(.*)~', pVal)
			if m:
				pVal = m.group(1)
			if not pVal:
				pVal = None
			foodItem[key] = pVal
		return foodItem