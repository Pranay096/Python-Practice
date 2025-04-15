x = 10
print (x)   # This will print the global variable x
def my_function():
    global x # This will refer to the global variable x
    x = 20 # this is a local variable
    y= 30 # this is also a local variable
    print(y)
my_function()      # This will print the local variable x
print (x)
# print(y) # This will raise an error because y is not a global variable
 
