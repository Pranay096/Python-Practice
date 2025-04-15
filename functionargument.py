# def name(fname, mname = "Tukaram", lname = "Pelapkar"):
#     print("Hello,", fname, mname, lname)

# name("Pranay")

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Gorakh", lname = "Tupe", fname = "Tanvi")

# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)
  
# average(8, 9)

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return(sum/len(numbers))
        
c = average(8, 8)
print(c)