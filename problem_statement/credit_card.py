#reference: https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/

def credit_card(card):

    if  len(card) == 16:

        for i in card[:12]:
           
            if i.isdigit():
            #if i <= 8:
                i = '*'
                print(i, end='')   
                
                #break
            else:
                print("It is not a credit")    
        print(card[12:16])
    else:
        print("it is a not credit card")    

credit_card("123e567891234567") 

