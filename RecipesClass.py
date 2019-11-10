import os


class Recipes:
    
    def __init__(self, name, ingNames, ingAmounts, timeType, difficulty, instructions):
        self.name = name
        self.ingNames = ingNames
        self.ingAmounts = ingAmounts
        self.timeType = timeType
        self.difficulty = difficulty
        self.instructions = instructions

    def getName(self):
    	return self.name

    def getIngNames(self):
        return self.ingNames

    def getIngAmounts(self):
        return self.ingAmounts

    def getTimeType(self):
    	return self.timeType

    def getDifficulty(self):
    	return self.difficulty

    def getInstructions(self):
    	return self.instructions











