def fibo(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
p=int(input("Enter number for fibonacci series: "))
for i in range(p):
    print(fibo(i),end=" ")
