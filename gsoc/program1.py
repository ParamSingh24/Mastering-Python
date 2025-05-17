#Sieve of Eratosthenes

def Sieve(n):
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    for i in range (2,int(n**0.5)+1):
        if prime[i]:
            for j in range (i*i,n+1,i):
                prime[j]=False 
    l = []
    for k in range (2,n+1):
        if prime[k]:
            l.append(k)
    print(l)    

Sieve(int(input("Enter number till you want to Find Prime Numbers:")))
