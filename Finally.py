def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Execution of the try-except block is complete.")

# Example usage
divide_numbers(10, 2)
divide_numbers(10, 0)

try:
    l = [1, 2, 3, 4, 5]
    i=int(input("Enter a index: "))
    print(l[i])
except:
    print("Index out of range.")
finally:
    print("Execution of the try-except block is complete.")