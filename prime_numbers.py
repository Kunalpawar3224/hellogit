#First program for first 100 prime numbers 
#First impletation 
#Will convert this in the class

def isprime(n):
    if(n==0 or n==1):
      return False

    for i in range(2,n):
      if(n%i==0):
       return False

    return True

def first_primes():
  check_prime=[]
  for i in range(3434):
    if (isprime(i)):
        
        a = len(check_prime) 
        if (a==100):
          break
    
        check_prime.append(i)
  return check_prime

if __name__ == '__main__':     
  primes = first_primes()
  print(len(primes))      
  print(primes)
