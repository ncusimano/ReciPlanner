from RecipePlannerClass import RecipePlanner
import RecipesClass




if __name__ == "__main__":

	myPlanner = RecipePlanner()
	myPlanner.getRecipes()	
	
	myPlanner.makeRecipe("Noodles", ["Packets", "Water"], [2, 1], "Breakfast", 1, "- Boil water\n- Add packets\n- more liness\n- yay")

	myPlanner.makeRecipe("New", ["ing1", "ing2", "ing3"], [1, 2, 3], "Dinner", 2, "Instructions")

	myPlanner.editRecipe("New2", ["ing1", "ing2", "ing3"], [1, 2, 3], "Lunch", 2, "Instructions", "New")
