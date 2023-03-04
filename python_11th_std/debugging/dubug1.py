import pdb

a = int(input("Enter a number: "))
j = a
for i in range(4):
    pdb.set_trace()
    print(j**i)