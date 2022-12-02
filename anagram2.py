def anagram():
    '''
    Implementation of Anagram problem statement
    '''
    str1_list =[]
    str2_list =[]
    
    f= open("/home/kunal/anagram.txt", "r")
    
    a=f.readline()

    while a:
        
        a1 = sorted(a)

        with open ("/home/kunal/anagram.txt") as file:
            for i in file :

                i1 = sorted(i)
                 
                if len(a) == len(i):
                    #Look for the possible anagrams from the strings which has equal lengths

                    if a==i :
                        continue
                        #skip the given string, because it occurs two times in the output

                    elif a1 == i1 :
                        #Confirmation of the anagram, by comparing sorted string
                        str1_list.append(i.strip())                        
                        print(a.strip(), str1_list)      
                str1_list.clear()           
        a=f.readline()                      
                                        
anagram()