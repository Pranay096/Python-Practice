x = int(input("Enter the value of x: "))

match x:
    
    case 0:
        print("Case is 0")
        
    case 4:
        print("Case is 94")
        
    case _ if x!=90:
        print(x, "is not 90")
        
    case _ if x!=79:
        print(x, "is not 79")
        
    case _:
        print(x)