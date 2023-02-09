'''
lec4
dict and tuple
'''

my_tuple = 'a', 'b', 'c', 'd', 'e'
print(my_tuple)

print(  type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:2])

#my_tuple[0] = 'f'
#print( my_tuple[0])
# Cannot do this because you cannot change the values in a tuple.

my_car = { 
        'color':'silver',
        'maker':'mercedes',
        'year':2007
          }
print(my_car)
print(my_car['maker'])
print(my_car['year'])

print(my_car.items())
print(my_car.keys())
print(my_car.values())

#same result 
print(my_car.get('color'))
print(my_car['color'])

my_car['model'] = 'c-class'
print(my_car)

my_car['year'] = 2021
print(my_car)

print(  len(my_car)   )

print(  'color' in my_car)
print(  'red' in my_car.values())