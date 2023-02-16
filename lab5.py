'''

Lab 5
If Statement in Python 

'''

#3.1 
alien_color = 'yellow'

if alien_color == 'green':
    print('you got 5 points')
    
#3.2
alien_color = 'pink'

if alien_color == 'green':
    print('you got 5 points')
else:
    print('you got 10 points')
    
#3.3
favorite_fruits = ['mangos','blueberries','oranges']

if 'strawberries' in favorite_fruits:
    print('You really like bananas!')
if 'mangos' in favorite_fruits:
    print('You really like bananas!')
if 'grapes' in favorite_fruits:
    print('You really like bananas!')

#3.4
age = 88

if age < 10:
    print('They are a kid.')
elif age < 20:
    print('They are a teenager.')
else:
    print('They are an adult.')
    if age > 65:
        print('They are an elder.')

    


