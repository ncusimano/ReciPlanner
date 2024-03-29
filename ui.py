import pygame, sys, time, calendar as cal
from math import *
from pygame.locals import *
from random import randint

import Calendar as ca
import RecipePlannerClass as RP
import ingredient_list_lol as il
import Grocery_List as GL

import test_ui as tu
import disp_recipe as dr
import display_gross_lst as dg


pygame.init()
pygame.font.init()



class ui:
	def __init__(self):
		self.WINDOWWIDTH = 1000
		self.WINDOWHEIGHT = 640
		self.window_Surface = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT), 0, 32)
		pygame.display.set_caption('ReciPlanner')



		self.tabs = [pygame.Rect(3,3,80,16),pygame.Rect(87,3,80,16),pygame.Rect(171,3,80,16),pygame.Rect(255,3,80,16)]
		self.tabFont = pygame.font.Font(None, 16)



		self.scrollpos = 0



		self.recipe_planner = RP.RecipePlanner()
		self.ingredient_list = il.Ingredient_List()
		self.grocery_list = GL.GroceryList()

		self.grocery_list.recreateGross()
		self.ingredient_list.recreateDict()
		self.recipe_planner.loadRecipes()

		self.food_calender = ca.FoodCalendar(self.recipe_planner.getRecipeList(),self.ingredient_list,self.grocery_list)



		self.food_calender.loadDays()



		self.Recipe_Tab = list_recipe(self)
		self.Calender_Tab = calender(self)
		self.Ingredients_Tab = list_ingredients(self)
		self.Groceries_Tab = list_groceries(self)

		self.tab_list = [self.Calender_Tab,self.Recipe_Tab,self.Ingredients_Tab,self.Groceries_Tab]

		self.selected_tab = self.Calender_Tab
		self.tabs[self.selected_tab.number].y += 4
		self.tab_biscuits = self.Calender_Tab.biscuits
		


		self.list_font = pygame.font.Font(None, 24)



		self.colour_theme = colour.LIGHT
		self.colour_theme_shadow = self.shadow(self.colour_theme)

	def run(self):
		#Get und interpret events
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.font.quit()
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				self.tab_select(event)
				self.scroll = scrolltest(event)
				self.scrollpos -= self.scroll
				for biscuit in self.tab_biscuits:
					if biscuit.rect.collidepoint(event.pos):
						biscuit.func(self.selected_tab)


		#Check Section

		#Draw to screen
		self.window_Surface.fill(self.colour_theme_shadow)
		self.selected_tab.draw()

		#print to screen
		pygame.display.update()

	def tab_select(self, event):
		for i, j in enumerate(self.tabs):
			if j.collidepoint(event.pos):
				self.scrollpos = 0
				self.tabs[self.selected_tab.number].y = 3
				self.selected_tab = self.tab_list[i]
				self.tabs[self.selected_tab.number].y += 4
				self.tab_biscuits = self.selected_tab.biscuits
				break

	def expired_question(self, list):
		pass

	def draw_tab_labels(self, num):
		pygame.draw.rect(self.window_Surface, self.colour_theme, pygame.Rect(3,23,992,612))
		for i, j in enumerate(["Calender", "Recipes", "Ingredients", "Grocery List"]):
			pygame.draw.rect(self.window_Surface, self.colour_theme, self.tabs[i])
			self.window_Surface.blit(self.tabFont.render(j,True,colour.DARK), self.tabs[i])

	def shadow(self, colour):
		temp = [0,0,0]
		for i in range(0,3):
			temp[i] = ((colour[i]+1) * 3 / 4)-1
		return temp



#			 #
#  CALENDER  #
#			 #
class calender:
	number = 0
	def __init__(self, master):
		self.master = master
		self.recipe_calender = self.master.food_calender.getSetDays()
		self.day = None
		self.calender_font = pygame.font.Font(None, 16)
		self.update_month_biscuits()

	def update_calender(self):
		self.recipe_calender = self.master.food_calender.getSetDays()

	def update_month_biscuits(self):
		self.biscuits = []
		day0 = int(self.recipe_calender[0].date[1])-1
		for day in self.recipe_calender:
			self.biscuits.append(biscuit(pygame.Rect(20+(88*int(day.date[1])),31+((int(day.date[0])+day0)//7)*88,72,72),str(day.date[0]),self.biscuit_month_wrapper(int(day.date[0]))))
		self.master.tab_biscuits = self.biscuits

	def update_day_biscuits(self):
		self.biscuits = []
		i=0
		self.biscuits.append(biscuit(pygame.Rect(7,31,64,32),"Back", self.biscuit_back_wrapper()))
		for recipe in self.recipe_calender[self.day].recipes:
			self.biscuits.append(biscuit(pygame.Rect(7,71+(i*40),256,32),recipe.name, self.biscuit_day_wrapper(recipe)))
			i+=1
		if self.recipe_calender[self.day].shopping:
			self.biscuits.append(biscuit(pygame.Rect(7,71+(i*40),256,32),"Grocery Day", lambda x: None))
		self.master.tab_biscuits = self.biscuits

	def draw(self):
		self.master.draw_tab_labels(0)
		for biscuit in self.biscuits:
			pygame.draw.rect(self.master.window_Surface, [200,200,200], biscuit.rect)
			self.master.window_Surface.blit(self.calender_font.render(biscuit.text, False, colour.DARK), biscuit.rect)

	def biscuit_day_wrapper(self,recipe):
		def func(calender):
			r = veiw_recipe(recipe)
			r.run()
		return func

	def biscuit_month_wrapper(self, number):
		def func(calender):
			calender.day=number
			calender.update_day_biscuits()
		return func

	def biscuit_back_wrapper(self):
		def func(calender):
			calender.day = None
			calender.update_month_biscuits()
		return func


class add_recipe_to_calender: # add recipes to calender
	def __init__(self):
		pass


#			#
#  RECIPES  #
#			#
class list_recipe:
	number = 1
	biscuits = []
	def __init__(self, master):
		self.master = master
		self.recipes = self.master.recipe_planner.getRecipeList()
		self.load_biscuits(self.master.scrollpos)

	def load_biscuits(self, num):
		self.biscuits=[]
		if num+10>len(self.recipes):
			num = len(self.recipes)
		if num < 0:
			num = 0
		if len(self.recipes)<10:
			for i in range(0,len(self.recipes)):
				self.biscuits.append(biscuit(pygame.Rect(7,71+(num-i)*40,256,32),self.recipes[i].name, self.veiw_wrapper(self.recipes[i])))
		else:
			for i in range(num, num+10):
				self.biscuits.append(biscuit(pygame.Rect(7,71+(num-i)*40,256,32),self.recipes[i].name, self.veiw_wrapper(self.recipes[i])))
		self.biscuits.append(biscuit(pygame.Rect(7,431,128,32),"Add New recipe", self.new_wrapper()))

	def veiw_wrapper(self, recipe):
		def func(parameter):
			dr.main(recipe)
		return(func)

	def new_wrapper(self):
		def func(parameter):
			tu.main(parameter.master.recipe_planner)
			parameter.master.recipe_planner.getRecipeList()
			parameter.master.Recipe_Tab.load_biscuits(parameter.master.scrollpos)
		return func

	def draw(self):
		self.master.draw_tab_labels(0)
		for biscuit in self.biscuits:
			pygame.draw.rect(self.master.window_Surface, [200,200,200], biscuit.rect)
			self.master.window_Surface.blit(self.master.list_font.render(biscuit.text, False, colour.DARK), biscuit.rect)




#				#
#  INGREDIENTS  #
#				#
class list_ingredients:
	number = 2
	biscuits=[]
	def __init__(self, master):
		self.master = master
		self.master.ingredient_list.recreateDict()
		self.ingredients = self.master.ingredient_list.getNameList()
		self.load_biscuits(self.master.scrollpos)

	def load_biscuits(self, num):
		self.biscuits=[]
		if num+10>len(self.ingredients):
			num = len(self.ingredients)
		if num < 0:
			num = 0
		if len(self.ingredients)<10:
			for i in range(0,len(self.ingredients)):
				self.biscuits.append(biscuit(pygame.Rect(7,71+(num-i)*40,256,32),self.ingredients[i], lambda x: None))
		else:
			for i in range(num, num+10):
				self.biscuits.append(biscuit(pygame.Rect(7,71+(num-i)*40,256,32),self.ingredients[i], lambda x: None))

	def new_wrapper(self):
		def func(parameter):
			r = add_ingredients()
			r.run()
		return func

	def draw(self):
		self.master.draw_tab_labels(0)
		for biscuit in self.biscuits:
			pygame.draw.rect(self.master.window_Surface, [200,200,200], biscuit.rect)
			self.master.window_Surface.blit(self.master.list_font.render(biscuit.text, False, colour.DARK), biscuit.rect)

class add_ingredients:
	def __init__(self, master):
		pass
	def run(self):
		pass

#
#
#
class list_groceries:
	number = 3
	biscuits=[]
	def __init__(self, master):
		self.master = master
		self.load_biscuits(self.master.scrollpos)

	def load_biscuits(self, num):
		self.biscuits=[]
		self.groceries = self.master.grocery_list.checkRefill(self.master.ingredient_list)
		if num+10>len(self.groceries):
			num = len(self.groceries)
		if num < 0:
			num = 0
		if len(self.groceries)<10:
			for i in range(0,len(self.groceries)):
				self.biscuits.append(biscuit(pygame.Rect(7,71+(num-i)*40,256,32),self.groceries[i], lambda x: None))
		else:
			for i in range(num, num+10):
				self.biscuits.append(biscuit(pygame.Rect(7,71+(num-i)*40,256,32),self.groceries[i], lambda x: None))

	def draw(self):
		self.master.draw_tab_labels(0)
		for biscuit in self.biscuits:
			pygame.draw.rect(self.master.window_Surface, [200,200,200], biscuit.rect)
			self.master.window_Surface.blit(self.master.list_font.render(biscuit.text, False, colour.DARK), biscuit.rect)


#			 #
#  SETTINGS  #
#			 #
class settingsUi:
	def __init__(self, master):
		pass


# DRAW BISCUITS #
class biscuit:
	def __init__(self, rect, text, func):
		self.rect = rect
		self.text = text
		self.func = func
	def draw(self, surface, colour):
		pygame.draw(surface, colour, self.rect)



#  FUNCTIONS FOR SPECIAL THINGS
def scrolltest(event):
	if event.type == MOUSEBUTTONDOWN:
		if event.button == 4:
			return 1
		elif event.button == 5:
			return -1
		else:
			return 0



class colour:
	LIGHT = [255,255,255]
	DARK = [64,64,64]
	GREY = [128,128,128]
	BREAKFAST = [255,255,0] #yellow
	LUNCH = [0, 255, 0] #Green
	DINNER = [0,0,255] #Blue
	SNAKE = [255,0,0] #Red/burgundy/wine




r = ui()
while True:
	r.run()