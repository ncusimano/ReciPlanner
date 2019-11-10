class Ingredient_List:
    def __init__(self):
        self.dict_list = {}
        
        

    def __str__(self):
        return str(self.dict_list)
        
    def getDict(self):
    	return self.dict_list
    

    #VERY IMPORTANT RUN EVERY TIME PROGRAM STARTS
    def recreateDict(self):
    	try:
    		with open("ingred_repository.txt", "r") as fin:
    			reading = True


    			while reading:
    				try:
    					curr_key = fin.readline().rstrip()

    					if curr_key =="":
    						raise NameError

    					curr_day = fin.readline().rstrip()
    					curr_month = fin.readline().rstrip()
    					curr_year = fin.readline().rstrip()
    					curr_amount = fin.readline().rstrip()

    					self.dict_list[curr_key] = [curr_day, curr_month, curr_year, curr_amount]

    				except NameError:
    					reading = False

    	except FileNotFoundError:
    		pass

    
    # list of strings with ingredient list
    def getNameList(self):
        return list(self.dict_list.keys())
    
    
    def add_item(self, name, day, month, year, amount):
    	#title class with ingred name
        #ingred_name = Ingredient(name, exp, amount)
        amount = float(amount)
        #print("TEST BOTT")
        self.dict_list[name] = [day,month,year, amount]
        self.SaveToRepo()


    def SaveToRepo(self):
        #print('hello ThErE')
        
        with open('ingred_repository.txt', 'w') as fin:
            for key in self.dict_list:
                [curr_day, curr_month, curr_year, curr_amount] = self.dict_list[key]
                    
                fin.write(key + "\n")
                fin.write(str(curr_day) + '\n')
                fin.write(str(curr_month) + '\n')
                fin.write(str(curr_year) + '\n')
                fin.write(str(curr_amount) + '\n')
        
        

        
    def del_item(self, name_to_delete):
        
        del self.dict_list[name_to_delete]
        self.SaveToRepo()
                
                
    def change_amount(self, state_val, key, amount_change):
        """
            For changing the amount of an ingredient
            Inputs: state_val for determining if increasing or decreasing
                    if 0: dec
                    if 1: inc
                    
                    key is name of item to change
            
            Changed dictionary to specifications, writes to file
        """
        warning = ''
        
        if state_val == 0:
            [a,b,c, current_amount] = self.dict_list[key]
            new_amount = current_amount - amount_change
            
            if new_amount <= 0:
                new_amount = 0
                warning = 'you are totally out of ' + str(key) + ', dude'

            self.dict_list[key] = [a,b,c, new_amount]
            
        elif state_val == 1:
            [e,f,g, current_amount] = self.dict_list[key]
            new_amount = current_amount + amount_change
            
            self.dict_list[key] = [e,f,g, new_amount]
            
        else:
            pass
        
        self.SaveToRepo()
        
        if warning != '':
            return warning
        
        
        #open
            # print whole dictionary to text file
        #close file
    def mockIngrList(self):
        a = Ingredient_List()
        a.recreateDict()
        a.add_item("PoTaToEs", 1, 12, 2019, 7)
        a.add_item("ToMaToEs", 12, 12, 2000, 90000)
        return a



'''
if __name__ == '__main__':
	a = Ingredient_List()
	a.recreateDict()
	a.add_item("PoTaToEs", 1, 12, 2019, 7)
	a.add_item("ToMaToEs", 12, 12, 2000, 90000)


	print(a)

'''


