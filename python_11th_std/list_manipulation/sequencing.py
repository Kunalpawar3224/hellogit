l1 = list('hello')
print(l1)    #it will print ['h', 'e', 'l', 'l', 'o']


t = ('w','e','r','t','y')

l2 =  list(t)
print(l2)   # it will print ['w', 'e', 'r', 't', 'y']
print(type(l2)
)

l3 = list(input('Enter list elements: '))    #23,34,5 4    if ur input is this then 

print(l3)                                    #['2', '3', ',', '3', '4', ',', '5', '4']   u will get output as this
print(type(l3))                                    # in string format

# If u want the output in integer then use  eval(input())
l4 = eval(input('Enter list elements: '))        #input = 23,34,45                  
print(l4)                                        #output = (23, 34, 45)
print(type(l4))

a = eval('5+8')
print(a)   # o/p= 13

y = eval("3*19")
print(y)     # 57

# eval() takes only integer values
k = eval(input("Enter value: "))    #i/p = 13123,3123
print(k, type(k))                   #o/p= (13123, 3123) <class 'tuple'>