#import Calendar

from datetime import datetime

class GroceryList:
	def __init__(self):
		self.gross_list = {}

	def checkRefill(self, itemName, expiryMonth, quantity):
		#later implement automatic adding to grocery list

		if datetime.now().month == int(expiryMonth):
			return "Your " + itemName + " has/have expired. Want to refill?"
			#passed to manager. manager will pass to ui
		elif float(quantity) == 0:
			return "You're out of " + itemName + ". Want to refill?"
		else:
			return ""

	def addItem(self, itemName, neededAmount):
	    neededAmount = float(neededAmount)
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
	print(a.checkRefill("hi", "12", 1))

	a.addItem("smiles", 5)
	
'''