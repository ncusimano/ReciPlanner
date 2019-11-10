from RecipePlannerClass import RecipePlanner
import RecipesClass




if __name__ == "__main__":

	myPlanner = RecipePlanner()
	myPlanner.loadRecipes()	
	
	myPlanner.makeRecipe("Noodles", ["Packets", "Water"], [2, 1], "Breakfast", 1, "- Boil water\n- Add packets\n- more liness\n- yay")
