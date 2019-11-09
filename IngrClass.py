class Ingredient:
	def __init__(self, name, expiry, amount):
		self.name = name
		self.expiry = expiry
		self.amount = amount

	def getName(self):
		return self.name

	def getExpDate(self):
		return self.expiry

	def getQuantity(self):
		return self.amount

	def getTable(self):
		return self.name, self.expiry, self.amount
