import os

def count_python_files(directory):
    count = 0
    for file in os.listdir(directory):
        if file.endswith('.py'):
            count += 1
    return count

directory = "d:/python practice"
total_files = count_python_files(directory)
print(f"Total number of Python files in '{directory}': {total_files}")