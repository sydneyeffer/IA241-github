'''
lec 9
define class
'''

def report_maker(input):
    
    return input
    
class car: 
    maker = 'toyota'
    
 #   def report_maker(self):
        
 #       return self.maker,123
 
 def __init__(self,input_model):
     self.model = input_model
    
my_car_instance = car('highlander') 
print(my_car_instance.maker)
print(my_car_instance.model)