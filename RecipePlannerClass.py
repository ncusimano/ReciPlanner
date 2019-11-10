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
        self.saveRecipe(recipe_new)

    def numSaveLines(self, file):
        with open(file) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

   # Saves edited or new recipies to their own file in a recipe directory. 
    def saveRecipe(self, recipe):
        current_path = os.getcwd()

        if not os.path.isdir("Recipies"):
            os.mkdir("Recipies")

        current_path += "\\Recipes" + "\\" + recipe.name + ".txt"

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