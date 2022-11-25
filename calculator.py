print('For addition enter: 1')
print('For substraction enter: 2')
print('For multiplication enter: 3')
print('For division enter: 4')

choice = int(input('Enter your choice: '))

if  choice in (1,2,3,4 ):
    a= int(input('Enter your first number '))
    b= int(input('Enter your second number '))

    if choice == 1 :
        print(a+b)
    elif choice == 2:
        print(a-b)
    elif choice == 3:
        print(a*b)
    elif choice == 4:
        print(a/b)
else:
    print('enter valid choice')