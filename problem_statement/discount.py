#reference: https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/

def discount(original, discounted):

    try:
        #if isinstance(original & discounted, int):
            current_price = original - discounted
            print(current_price)
            return current_price
    except:
        print("Please enter valid values")

discount(20, "d")