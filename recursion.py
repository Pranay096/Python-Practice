def factorial(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n*factorial(n-1)
    
def print_range(i):
    for p in range(i,1,-1):
        print(p,end="*")
    print(1)
    
n=int(input("Enter your number: "))
print_range(n)
print("=",factorial(n))