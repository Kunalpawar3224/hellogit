'''
First implementation of codekata kata02: karate chop
link of problem statement as follows
http://codekata.com/kata/kata02-karate-chop/
will implement using binary search
'''

def chop( num, list_index):
   
    print("Elements in the list:", list_index)
    print("check the",num,"is exist inside the list or not")

    if num in list_index:
        index = list_index.index(num)
        print(num, "is present at the index", index)
    else:
        print("-1")

list_index =[1,3,5]
num = 5
 
chop(num, list_index)   