#reference: https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/

def credit_card(card):
    if len(card) == 16:
        print("it is a credit card")

        for i in card[:12]:
                
            #if i <= 8:
                i = '*'
                print(i, end='')   
        print(card[12:16])
    else:
        print("it is a not credit card")    

credit_card("4444444444444444")        
