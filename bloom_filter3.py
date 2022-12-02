class bloom_filter :
    '''
    Bloom filter implementation
    '''
    array =  [True,True,True,True,True,True,True,True,True]
    k=0
    train_list = [] 
    train = ['cat', 'dog', 'parrot']
    user=['monkey', 'dog']

    def train_(self,array,train) :
            
        for i in train:
            print(i)
            self.train_list.append(len(i))
            self.array = array
            
            if array[len(i)] == True:
                array[len(i)]=False
            elif array[len(i)] != True :   
                array[len(i)]=False
        #print(array)
        return array

    result =train([True,True,True,True,True,True,True,True,True], ['cat','dog','parrot'])
    #print(array)
    print(result)
    #print(array)

