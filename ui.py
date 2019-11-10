import pygame, sys, time
from math import *
from pygame.locals import *
from random import randint

pygame.init()
pygame.font.init()

class ui:
	def __init__(self):
		self.WINDOWWIDTH = 640
		self.WINDOWHEIGHT = 640
		self.window_Surface = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT), 0, 32)
		pygame.display.set_caption('ReciPlanner')



		self.tabs = [pygame.Rect(3,3,80,16),pygame.Rect(87,3,80,16),pygame.Rect(171,3,80,16),pygame.Rect(255,3,80,16)]
		self.tabFont = pygame.font.Font(None, 16)

		self.Recipe_Tab = list_recipe(self)
		self.Calender_Tab = calender(self, ["HALP","ME"])
		self.Ingredients_Tab = list_ingredients(self)
		self.Groceries_Tab = list_groceries(self)

		self.tab_list = [self.Calender_Tab,self.Recipe_Tab,self.Ingredients_Tab,self.Groceries_Tab]

		self.selected_tab = self.Calender_Tab
		self.tabs[self.selected_tab.number].y += 4
		


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
				self.tab_select(self, event)


		#Check Section

		#Draw to screen
		self.window_Surface.fill(self.colour_theme_shadow)
		self.selected_tab.draw()

		#print to screen
		pygame.display.update()

	def tab_select(self, master, event):
		for i, j in enumerate(self.tabs):
			if j.collidepoint(event.pos):
				self.tabs[self.selected_tab.number].y = 3
				self.selected_tab = self.tab_list[i]
				self.tabs[self.selected_tab.number].y += 4
				break

	def expired_question(self, list):
		pass

	def draw_tab_labels(self, num):
		pygame.draw.rect(self.window_Surface, self.colour_theme, pygame.Rect(3,23,632,612))
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
	def __init__(self, master, recipe_calender):
		self.master = master
		self.recipe_calender = recipe_calender

	def update_calender(recipe_calender):
		self.recipe_calender = recipe_calender

	def draw(self):
		self.master.draw_tab_labels(0)

		# if day == 0:
		# 	row = 0
		# 	for i in self.recipe_calender:
		# 		pygame.draw(master.window_Surface, colour.GREY, )
		# else:
		# 	for i in self.recipe_calender[day-1]:
		# 		pass


class add_recipes: # add recipes to calender
	pass


#			#
#  RECIPES  #
#			#
class veiw_recipe:
	def __init__(self, recipeObj): #recipeObj should have all the recipe data in it
		pass

class list_recipe:
	number = 1
	def __init__(self, master):
		self.master = master
		pass
	def draw(self):
		self.master.draw_tab_labels(0)

class add_recipe:
	def __init__(self,master):
		pass


#				#
#  INGREDIENTS  #
#				#
class list_ingredients:
	number = 2
	def __init__(self, master):
		self.master = master
		pass
	def draw(self):
		self.master.draw_tab_labels(0)

class add_ingredients:
	def __init__(self, master):
		pass


#
#
#
class list_groceries:
	number = 3
	def __init__(self, master):
		self.master = master
		pass
	def draw(self):
		self.master.draw_tab_labels(0)


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