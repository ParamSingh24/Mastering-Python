#TO calculate the gcd of two number 
def gcd(a,b):
    while b != 0:
        a , b = b , a%b
    return a 
n = int(input("enter number:"))
b = int(input("enter number:"))
g = gcd(n,b)
print(f"the gcd of two numbers are {g}")




