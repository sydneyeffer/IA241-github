'''
lab7
while Loop in Python
'''

#3.1
i = 0

while i <= 5: 
    if i != 3:
        print(i)
    i += 1
 
#3.2
i = 1
result =1

while i<=5:
    result = result * i
    i = i +1
    
print(result)

#3.3
result = 0
i=1
while i>=5:
    result = result +i
    i=i+1
    
print(result)

#3.4
i = 3
result = 1

while i <= 8:
    result = result*i
    i +=1 
    
print(result)

#3.5
i  = 4
result = 1 
while i <= 8:
    result = result *i
    i = i +1
print(result)


#3.6
num_list = [12, 32, 43, 35]

while num_list:
    num_list.pop()
    print(num_list) 


