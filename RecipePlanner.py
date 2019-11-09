import RecipesClass
import pickle
import ingredient_list_lol

class RecipePlanner(object):

    def __init__(self, recipe): 
        self.__recipe_list = [recipe]
        self.getRecipes()

    def getRecipeList():
        return self.__recipe_list

    def getRecipes():
        pass


    def makeRecipe(self, name, ingredientsList, timeType, difficulty, instructions):

        recipe = RecipesClass(name, ingredientsList, timeType, difficulty, instructions)
        recipe.saveRecipe()

        return






            
