# #reference: https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/

# def credit_card(card):

#     if  len(card) == 16:

#         for i in card[:12]:
           
#             if i.isdigit():
#             #if i <= 8:
#                 i = '*'
#                 print(i, end='')   
#                 #break
#             else:
#                 print("It is not a credit")    
#         print(card[12:16])
#     else:
#         print("it is a not credit card")    

# credit_card("123e567891234567") 

cc = '456364607935616'

def maskify(cc):
    new_string = ''
    if len(cc) > 4:
        new_string += '#' * (len(cc) - 4) + cc[-4:]
    else:
        return cc
    return new_string

print(maskify(cc))

