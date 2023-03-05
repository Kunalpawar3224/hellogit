l1 = ['a','e', 'i','o','u',['k','p']]

print(l1[2])
print(l1[-3])
print(len(l1))
print(l1[5])   #o/p= ['k','p']
print(l1[3:-1])

print('a' in l1)
print('a' not in l1)
print('A' not in l1)

l1[2] = 'm'   # lists are mutable
print(l1)


for g in l1:
    print(g)

l2 , l3 = [1,2,3] , [1,2,3]
l4 = [1,[2,3]]

print(l2==l3) 
print(l2==l4)

print('just for understanding')
print([1,2,8,9]<[9,1])   # it will check first index 1<9
print([1,2,8,9]<[1,2,9,8])  # now it will check 2nd index 8<9

print(l1 + l2)
print(l2*3)

print("just a break to understand")
lst= [10,12,14,20,22,24,30,32,34]
print(lst[3:30])
print(lst[-15:7])

print(lst[0:10:2])
print(lst[::-1])   # it will give the reverse list

# using slices for list modification
L = ["one","two","three"]
L[0:2]=[0,1]
print(L)   # it will change indices of 0and 1 o/p = [0, 1, 'three']

L[0:2]="a"
print(L)  # o/p = ['a', 'three']

L1 = [1,2,3]
L1[2:]="604"
print(L1)   # o/p= [1, 2, '6', '0', '4']