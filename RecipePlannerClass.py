import os
import pickle
from RecipesClass import Recipes
import ingredient_list_lol


class RecipePlanner():

    def __init__(self): 
        self.__recipe_list = []

    def getRecipeList(self):
        return self.__recipe_list

    def getRecipes(self):
        path = os.getcwd() + "/Recipes"

        file_list = os.listdir(path = path)

        for file in file_list:
            recipe = []
            with open(path + "/" + file, 'r') as fin:
                for i in range(1, 6):
                    recipe.append(fin.readline())

                ins_str = ""
                for x in range(self.numSaveLines(path + "/" + file)):
                    ins_str += fin.readline()

                recipe.append(ins_str)


            recipe_obj = Recipes(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4], recipe[5])
            self.__recipe_list.append(recipe_obj)

    def makeRecipe(self, name, ingNames, ingAmounts, timeType, difficulty, instructions):
        recipe_new = Recipes(name, ingNames, ingAmounts, timeType, difficulty, instructions)

        for i in range(len(self.__recipe_list)):
            if recipe_new.getName() == self.__recipe_list[i].getName():
                return "That recipe name already exists."

        self.saveRecipe(recipe_new)

        self.__recipe_list.append(recipe_new)

    def editRecipe(self, name, ingNames, ingAmounts, timeType, difficulty, instructions, oldRecipeName):
        recipe_edited = Recipes(name, ingNames, ingAmounts, timeType, difficulty, instructions)

        self.saveRecipe(recipe_edited)

        if not recipe_edited.getName() == oldRecipeName:
            os.remove(os.getcwd() + "\\Recipes\\" + oldRecipeName +".txt" )


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




