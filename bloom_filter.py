

def bloom_filter(animals):
 '''
 Implementation of Bloom filter
 '''   
 hash_animal=[]
 for i in animals :
    hash_animal.append(hash(i))
    #created and stored hash values of every element for unique identification
     
 return hash_animal


def hash_animal():
    '''
    Hash values of every element stored
    '''
    return bloom_filter( ['cat', 'dog', 'parrot','rat', 'lion', 'tiger'])

def user(check_animal):
    '''
    Implementation of user to check the given element is present or not
    '''
    check_hash_animal =[]
    for k in check_animal:
        check_hash_animal.append(hash(k))
      
        for j in hash_animal():
         
                if hash(k)==j :
                    #hash values gives confirmation the element is present or not
                    print(k,': may be present')
                    break
                else :
                    print(k, "is definately not present")
    return 'definately not present'       

user_once = user(['eagle','cat','man','tiger','cat','mouse','lion'])

