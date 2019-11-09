class Recipes(object):
    def __init__(name, ingredientsList, timeType, difficulty, instructions):
    	self.name = name						# string
    	self.ingredientsList = ingredientsList	# list of 2-cell lists
    	self.timeType = timeType				# string
    	self.difficulty = difficulty			# integer
    	self.instructions = instructions		# string

	def getName(self):
		return self.name

	def getIngredientsList(self):
		return self.ingredientsList

	def getTimeType(self):
		return self.timeType

	def getDifficulty(self):
		return self.difficulty

	def getInstructions(self):
		return self.instructions

	









