'''
lab3
list and set in python
'''

#3.1
str_list = ['a','d','e','b','c']
print(str_list)

str_list.sort()
print(str_list)

#3.2
str_list.extend(['f'])
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
index = str_list.index('c')
print('The index of c:', index)

#3.5
my_list = ('a','123',123,'b','B','False',False, 123,None,'None')
print(set(my_list))
print(len(set(my_list)))

#3.6
countofwords = len("This is my third python lab.".split())
print("This is my third python lab.", countofwords)

#3.7
num_list = [12,32,43,35]
num_list.sort()
print(num_list[0])
print(num_list[-1])

#3.8
game_board = [ [0,0,0], [0,0,0], [0,0,0]  ]
print(game_board)
game_board[1] = [0,1,0]
print(game_board)







