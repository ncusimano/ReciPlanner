import Recipes
import pickle
from Ingredient_List import getNameList

class RecipePlanner(object):

    def __init__(self): 
        self.__recipe_list = []
        self.getRecipes()

    def getRecipeList():
        return self.__recipe_list

    def getRecipes():
        pass


    def makeRecipe(self, name, ingredientsList, timeType, difficulty, instructions):

        recipe = Recipes(name, ingredientsList, timeType, difficulty, instructions)
        recipe.saveRecipe()

        return






            
