from RecipePlannerClass import RecipePlanner
from Grocery_List import GroceryList
import os
from DayClass import Day
from ingredient_list_lol import Ingredient_List

# BIG BIG BOI
class FoodCalendar():
	def __init__(self, all_recipes, all_ingredients, grocery_list):
		self.__set_dates = []
		self.__all_recipes = all_recipes # List of recipe objects from existing Recipe Planner obj.
		self.__all_ingredients = all_ingredients # List of all ingredients from existing Ingredients List obj.
		self.__grocery_list = grocery_list # Existing Grocery List obj.

	def getSetDays(self):
		return self.__set_dates

	def loadDays(self):
		path = os.getcwd() + "/CalendarLog"

		file_list = os.listdir(path = path)

		for file in file_list:
			with open(path + "/" + file, 'r') as fin:
				# Splits all entries in the file by type.
				entries = fin.readlines()

			# Gets the date as a list.
			date = entries[0].split(',')

			# Retrieves recipe names from the entries.
			recipe_names = entries[1].split(',')

			# Fishes the recipe objects out of the full recipe list based on name.
			recipes = []
			for name in recipe_names:
				i = 0
				searching = True
				while searching and i < len(self.__all_recipes):
					if name == self.__all_recipes[i].getName():
						recipes.append(self.__all_recipes[i])
						searching = False
					else:
						i += 1

			expiries = self.__grocery_list.checkRefill(self.__all_ingredients)

			'''
			# Retrieves the expiry dates from the entries.
			expiry_dates = list(entries[2].split(','))
			ingredient_keys = all_ingredients.getNameList()

			# Fishes the keys (name) for the expiring ingredients out of the dictionary of all ingredients by date.
			for date in expiry_dates:
				for ingr in all_ingredients:
					if date[0] == all_ingredients[ingr][0] and date[1] == all_ingredients[ingr][1] and date[2] == all_ingredients[ingr][2]:
						expiries.append(ingr)
			'''

			# Retrieves the boolean specifying shopping dates from the file.
			shopping = bool(entries[2])

			self.__set_dates.append(Day(date, recipes, expiries, shopping))

	def saveDay(self, day):
		if not os.path.isdir("CalendarLog"):
			os.mkdir("CalendarLog")

		current_path = os.getcwd() + "/CalendarLog/{}.{}.{}.txt".format(day.date[0], day.date[2], day.date[3])

		with open(current_path, 'w') as fout:

			fout.write(str(day.date[0]) + ',' + str(day.date[1]) + ',' +  str(day.date[2]) + ',' + str(day.date[3]) + '\n')
			for item in day.recipes:
				fout.write(str(item) + ',')
			fout.write("\n")

			fout.write(str(day.shopping) + '\n')

	def makeDay(self, date, recipes, expiries, shopping):
		new_day = Day(date, recipes, expiries, shopping)
		self.saveDay(new_day)

	def addRecipe(self, day, recipe):
		day.recipes.append(recipe)
		saveDay(day)

	def removeRecipe(self, day, recipe):
		for item in day.recipes:
			if item == recipe:
				del item

		self.saveDay(day)

	def toggleShopping(self, day):
		day.shopping = not day.shopping

		self.saveDay(day)

'''
if __name__ == "__main__":
	thingy = Ingredient_List()

	stuffs = RecipePlanner()

	stuffs.loadRecipes()

	die = GroceryList()

	why = FoodCalendar(stuffs.getRecipeList(), thingy.mockIngrList(), die)

	why.makeDay([10, 4, 6, 2029], ["Pizza", 'Noodles'], [], False)

	why.loadDays()

	print(why.getSetDays())
'''
