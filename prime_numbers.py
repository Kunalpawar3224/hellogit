#First program for first 100 prime numbers 
#First impletation 
# Will convert this in the class

def isprime(n):
    if(n==0 or n==1):
      return False

    for i in range(2,n):
      if(n%i==0):
       return False

    return True

square=[]
for i in range(43345):
 if (isprime(i)):
    
     a = len(square) 
     if (a==100):
       break
 
     square.append(i)
    
print(len(square))      
print(square)