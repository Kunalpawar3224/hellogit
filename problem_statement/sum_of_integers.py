# Referencece: https://realpython.com/python-practice-problems/#problem-description

def add_it_up():
    num = int(input("Enter youur number: "))
    sum = 0
    for i in range(0 ,num+1):
        sum += i
    print(sum)    

add_it_up()
