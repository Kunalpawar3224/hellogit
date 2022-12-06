def anagram():
    '''
    Implementation of Anagram problem statement
    '''
    anagrams={}
    num = 0
    
    with open ("C:\\Users\\Dell\\Documents\\wordlist.txt") as file:
        for i in file :
            i = i.strip()
            key = "".join(sorted(i))
                 
            if key in anagrams:
                anagrams[key].append(i)
                    #Look for the possible anagrams from the strings which has equal lengths
            else :
                anagrams[key] = [i]

            num +=1                    
        print(anagrams)
        print(num)                                
anagram()