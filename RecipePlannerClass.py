import os
from RecipesClass import Recipes
import ingredient_list_lol

class RecipePlanner():

    def __init__(self): 
        self.__recipe_list = [] # Initializing an emtpy list of recipe objects (main recipe list)

    # Allows access to private recipe list
    def getRecipeList(self):
        return self.__recipe_list 

    # Reads all files in the /Recipes directory and converts them to recipe objects
    # These objects are stored into the main recipe list
    def loadRecipes(self):
        path = os.getcwd() + "/Recipes"

        file_list = os.listdir(path = path)

        # Reads each file for recipe values
        for file in file_list:
            recipe = []
            with open(path + "/" + file, 'r') as fin:
                # Reads all recipe values except instructions
                for i in range(1, 6):
                    recipe.append(fin.readline())

                # Reads the recipe instructions (last remaining lines after reading values above)
                ins_str = ""
                for x in range(self.numSaveLines(path + "/" + file)):
                    ins_str += fin.readline()

                recipe.append(ins_str)

            # Adds each recipe object in the main recipe list
            recipe_obj = Recipes(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5])
            self.__recipe_list.append(recipe_obj)

    # Creates a new recipe object, saves into an individual recipe file, updates main recipe list
    def makeRecipe(self, name, ingNames, ingAmounts, timeType, difficulty, instructions):
        recipe_new = Recipes(name, ingNames, ingAmounts, timeType, difficulty, instructions)

        for i in range(len(self.__recipe_list)):
            if recipe_new.getName() == self.__recipe_list[i].getName():
                return "That recipe name already exists."

        self.saveRecipe(recipe_new)

        self.__recipe_list.append(recipe_new)

    # Edits recipe objects and files
    """
    def editRecipe(self, name, ingNames, ingAmounts, timeType, difficulty, instructions, oldRecipeName):
        recipe_edited = Recipes(name, ingNames, ingAmounts, timeType, difficulty, instructions)

        self.saveRecipe(recipe_edited)

        currentIndex = 0
        for i in range(len(self.__recipe_list)):
            if self.__recipe_list[i].getName() == oldRecipeName:
                currentIndex = i

        self.__recipe_list[currentIndex].name = name
        self.__recipe_list[currentIndex].ingNames = ingNames
        self.__recipe_list[currentIndex].ingAmounts = ingAmounts
        self.__recipe_list[currentIndex].timeType = timeType
        self.__recipe_list[currentIndex].difficulty = difficulty
        self.__recipe_list[currentIndex].instructions = instructions

        if not recipe_edited.getName() == oldRecipeName:
            os.remove(os.getcwd() + "\\Recipes\\" + oldRecipeName +".txt" )
            #del self.__recipe_list[]
    """


    def saveRecipe(self, recipe):
        current_path = os.getcwd()

        if not os.path.isdir("Recipes"):
            os.mkdir("Recipes")

        current_path += "\\Recipes" + "\\" + recipe.getName() + ".txt"

        with open(current_path, 'w') as f:
            names_str = ""
            amounts_str = ""
            for i in range(len(recipe.getIngNames())):
                names_str += recipe.getIngNames()[i] + ","
                amounts_str += str(recipe.getIngAmounts()[i]) + ","

            f.write(recipe.getName() + "\n")
            f.write(names_str + "\n")
            f.write(amounts_str + "\n")
            f.write(recipe.getTimeType() + "\n")
            f.write(str(recipe.getDifficulty()) + "\n")
            f.write(recipe.getInstructions())



    def sortRecipes(self, filType, filVal):
        sorted_list = []

        if filType == "timeType":

            for i in range(len(self.__recipe_list)):
                if self.__recipe_list[i].getTimeType() == filVal + "\n":
                    sorted_list.append(self.__recipe_list[i])

        elif filType == "difficulty":
            for i in range(len(self.__recipe_list)):
                if self.__recipe_list[i].getDifficulty() == str(filVal) + "\n":
                    sorted_list.append(self.__recipe_list[i])

        else: # sort by ingredient
            assert filType == "ingredient", "using else but not with ingredient sorting"
            for i in range(len(self.__recipe_list)):
                if filVal in self.__recipe_list[i].getIngNames():
                    sorted_list.append(self.__recipe_list[i])

        return sorted_list

    def numSaveLines(self, file):
        with open(file) as f:
            for i, l in enumerate(f):
                pass
        return i + 1




