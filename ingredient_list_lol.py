class Ingredient_list:
    def __init__(self):
        self.dict_list = {}

    def __str__(self):
        return str(self.dict_list)
    
    
    
    
    def add_item(self, name, exp, amount):
        #current = Ingredient(name, exp, amount)
        
        self.dict_list[name] = [exp, amount]
        
            
        #open
           # write(dictionary) to text file
        #close
        
        
    def del_item(self, name_to_delete):
        
        del self.dict_list[name_to_delete]
        
            
        #open
            #write(dictionary) to text file
        #close
        
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
            
            if new_amount < 0:
                new_amount = 0
                warning = 'you are totally out of this, dude'
            
            self.dict_list[key] = [a, new_amount]
            
        elif state_val == 1:
            [b, current_amount] = self.dict_list[key]
            new_amount = current_amount + amount_change
            
            self.dict_list[key] = [b, new_amount]
            
        else:
            pass
        
        if warning != '':
            return warning
        
        
        #open
            # print whole dictionary to text file
        #close file
        
        
        
        
        
        
        