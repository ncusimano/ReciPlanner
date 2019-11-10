import os
import pickle
import RecipesClass
import ingredient_list_lol


class RecipePlanner(object):

    def __init__(self, recipe): 
        self.__recipe_list = [recipe]
        self.getRecipes()

    def getRecipeList():
        return self.__recipe_list

    def getRecipes():
        path = os.getcwd() + "/Recipes"

        file_list = os.listdir(path = path)

        for file in file_list:
            recipe = ()
            with open(path + "/" + file, 'r') as fin:
                for i in range(1, 5):
                    recipe.append(fin.readline())

            recipe = RecipeClass(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4])
            self.__recipe_list.append(recipe)
                    

    def makeRecipe(self, name, ingredientsList, timeType, difficulty, instructions):
        recipe = RecipesClass(name, ingredientsList, timeType, difficulty, instructions)
        self.saveRecipe(recipe)
        return

    def editRecipe():
        pass

    # Saves edited or new recipies to their own file in a recipe directory. 
    def saveRecipe(self, recipe):
        path = os.getcwd() +"/Recipes" + "/" + self.name + ".txt"

        with open(path, 'w') as f:
            f.write(recipe.name + "\n")
            f.write(recipe.ingredientsList + "\n")
            f.write(recipe.timeType + "\n")
            f.write(recipe.difficulty + "\n")
            f.write(recipe.instructions)






            
