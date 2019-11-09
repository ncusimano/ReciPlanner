class Ingredient_List:
    def __init__(self):
        self.dict_list = {}
        
        

    def __str__(self):
        return str(self.dict_list)
    
    
    # list of strings with ingredient list
    def getNameList(self):
        return list(self.dict_list.keys())
    
    
    def add_item(self, name, exp, amount):
    	#title class with ingred name
        #ingred_name = Ingredient(name, exp, amount)
        amount = int(amount)
        #print("TEST BOTT")
        self.dict_list[name] = [exp, amount]
        self.SaveToRepo()
     
        
    


    def SaveToRepo(self):
        print('hello ThErE')
        
        with open('ingred_repository.txt', 'w') as fin:
            for key in self.dict_list:
                [curr_exp, curr_amount] = self.dict_list[key]
                    
                fin.write(key + "\n")
                fin.write(curr_exp + '\n')
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
            [a, current_amount] = self.dict_list[key]
            new_amount = current_amount - amount_change
            
            if new_amount <= 0:
                new_amount = 0
                warning = 'you are totally out of ' + str(key) + ', dude'
            
            self.dict_list[key] = [a, new_amount]
            
        elif state_val == 1:
            [b, current_amount] = self.dict_list[key]
            new_amount = current_amount + amount_change
            
            self.dict_list[key] = [b, new_amount]
            
        else:
            pass
        
        self.SaveToRepo()
        
        if warning != '':
            return warning
        
        
        #open
            # print whole dictionary to text file
        #close file
if __name__ == '__main__':
	a = Ingredient_List()
	a.add_item("PoTaToEs", "someyhing", 7)
	a.add_item("ToMaToEs", "datedateee", 90000)

        
        
