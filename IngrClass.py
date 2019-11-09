class Ingredient:
	def __init__(self, name, expiry, amount):
		self.name = name
		self.expiry = expiry
		self.amount = amount


	def getName(self):
		return self.name

	def getExpDate(self):
		return self.expiry

	def getAmount(self):
		return self.amount

	def __str__(self):
		return self.name, self.expiry, self.amount

