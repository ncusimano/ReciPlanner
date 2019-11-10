import os


class Recipes:
    def __init__(self, name, ingNames, ingAmounts, timeType, difficulty, instructions):
    	self.name = name						# string
    	self.ingNames = ingNames
        self.ingAmounts = ingAmounts
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











