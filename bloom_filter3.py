#def  bloom_filter():
'''
 Bloom filter implementation of simple logic for bloom filter problem statement
 http://codekata.com/kata/kata05-bloom-filters/
'''
array =  [True,True,True,True,True,True,True,True,True]
k=0
train_list = [] 
train = ['cat', 'dog', 'parrot']
#Elements which are stored 

user=['monkey', 'cat', 'mouse']
#Elements to check which are present or not

def  bloom_filter():
 '''bloom filter implementation'''
 for i in train:
   # print(i)
    train_list.append(len(i))
       
    if array[len(i)] == True:
        array[len(i)]=False
    elif array[len(i)] != True :   
        array[len(i)]=False
 print(train_list)
 return array

result = bloom_filter()
#print(array)
print(result)

def user_once():
 for i in user:
   #print(len(i))
    if array[len(i)]== True:
        print(i,': definately not present')
    elif array[len(i)]== False:
        print(i,': may be present')

result1 = user_once()
#print(result1)