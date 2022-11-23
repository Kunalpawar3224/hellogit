
def isprime(n):
    if(n==0 or n==1):
      return False

    for i in range(2,n):
      if(n%i==0):
       return False

     
    return True

squares=[]
for i in range(43345):
 if (isprime(i)):
    #if (len(squares) == 101):
     # break
     a = len(squares) 
     if (a==100):
       break
 
     squares.append(i)
'''a = len(squares)  
      if (a==100) 
      break'''      
print(len(squares))      
print(squares)