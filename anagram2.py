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
            else :
                anagrams[key] = [i]

    num_anagrams =0
    for _, words in anagrams.items():
        # _ it is use as a variable in looping

        if len(words) > 1:
            print(" ".join(words))
            #Have to print set of anagram words
            num_anagrams += 1
    print("-" * 20)
    print(num_anagrams)              

if __name__=='__main__':
    anagram()                                    
