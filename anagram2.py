def anagram():
    '''
    Implementation of Anagram problem statement
    '''
    str1_list =[]
    str2_list =[]
    number =[]
    f= open("/home/kunal/anagram.txt", "r")
    #
    
    a=f.readline()

    while a:
        #to find the anagram of a, a will iterate line by line
        
        a1 = sorted(a)

        #a=f.readline()
        with open ("/home/kunal/anagram.txt") as file:
            for i in file :

                i1 = sorted(i)
                 
                if len(a) == len(i):

                    if a==i :
                        continue

                    elif a1 == i1 :
                        #str1_list.append(i)
                        print(f"{a}{i}")
                                
        a=f.readline()                      
                                   
anagram()