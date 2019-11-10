import os
import pickle
from RecipesClass import Recipes
import ingredient_list_lol


class RecipePlanner():

    def __init__(self): 
        self.__recipe_list = []

    def getRecipeList():
        return self.__recipe_list

    def getRecipes(self):
        path = os.getcwd() + "/Recipes"

        file_list = os.listdir(path = path)

        for file in file_list:
            recipe = []
            with open(path + "/" + file, 'r') as fin:
                for i in range(1, 6):
                    recipe.append("")

            recipe_obj = Recipes(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4])
            self.__recipe_list.append(recipe_obj)
                    

    def makeRecipe(self, name, ingredientsList, timeType, difficulty, instructions):
        recipe_new = Recipes(name, ingredientsList, timeType, difficulty, instructions)
        self.saveRecipe(recipe_new)


   # Saves edited or new recipies to their own file in a recipe directory. 
    def saveRecipe(self, recipe):
        current_path = os.getcwd()

        if not os.path.isdir("Recipies"):
            os.mkdir("Recipies")

        current_path += "\\Recipes" + "\\" + recipe.name + ".txt"

        with open(current_path, 'w') as f:
            f.write(recipe.getName() + "\n")
            f.write(recipe.getIngredientsList() + "\n")
            f.write(recipe.getTimeType() + "\n")
            f.write(recipe.getDifficulty() + "\n")
            f.write(recipe.getInstructions())