#import Calendar
from ingredient_list_lol import Ingredient_List 
from datetime import datetime

class GroceryList:
	def __init__(self):
		self.gross_list = {}

	def getDict(self):
		return self.gross_list


	#VERY IMPORTANT RUN EVERY TIME PROGRAM STARTS
	def recreateGross(self):
		try:
			with open("gross_repository.txt", "r") as fin:
				reading = True
				while reading:
					try:
						curr_key = fin.readline().rstrip()

						if curr_key =="":
							raise NameError

						curr_amount = fin.readline().rstrip()
						self.gross_list[curr_key] = curr_amount
					except NameError:
						reading = False
		except FileNotFoundError:
			pass
	
	#this method returns a list of items that need to be considered for rebuying
	def checkRefill(self,ingred_num):
		#later implement automatic adding to grocery list
		consider_rebuy = []
		new_dict = ingred_num.getDict()

		for item in new_dict:
			[new_day, new_month, new_year, new_amount] = new_dict[item]
			if (float(new_amount) == 0):
				consider_rebuy.append(item)

			elif (datetime.now().year > int(new_year)):
				consider_rebuy.append(item)

			elif int(new_day) == "--":
				if (datetime.now().day == 1 and datetime.now().month == int(new_month)):
					consider_rebuy.append(item)

			elif int(new_day) != "--":
				if datetime.now().day == int(new_day) and datetime.now().month == int(new_month):
					consider_rebuy.append(item)

				#passed to manager. manager will pass to ui
		return consider_rebuy

	def addItem(self, itemName, neededAmount):
		neededAmount = float(neededAmount)

		if neededAmount != 0:
			self.gross_list[itemName] = neededAmount
			self.SaveToRepo()

	def SaveToRepo(self):
		with open('gross_repository.txt', 'w') as fin:
			for key in self.gross_list:
				curr_amount = self.gross_list[key]
				fin.write(key + "\n")
				fin.write(str(curr_amount) + '\n')
			
	 
'''

if __name__ == '__main__':
	a = GroceryList()
	pot = Ingredient_List()
	pot.add_item("PoTaToEs", 1, 12, 2019, 7)
	pot.add_item("ToMaToEs", 12, 12, 2019, 90000)
	print(datetime.now().year)

	print(a.checkRefill(pot))
	#a.recreateGross()
	#a.addItem("smiles", 5)
	#a.addItem("sadness", 4)
'''	
	
