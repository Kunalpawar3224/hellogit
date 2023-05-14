# Referencece: https://realpython.com/python-practice-problems/#problem-description

def add_it_up():
    
    
    try:
        num = int(input("Enter youur number: "))
        # sum = 0
        result = sum(range(num + 1))
        # for i in range(0 ,num+1):
        #     sum += i   
        # print(sum)    
    except TypeError:
        result = 0  
    print(result)    
    return result

add_it_up()

# def add_it_up(n):
    
#     try:
#         result = sum(range(n + 1))
#     except TypeError:
#         result = 0
#     print(result)    
#     return result
# add_it_up(9)
