# Task 1: Read a File and Handle Errors

try:
    filename=input("Enter the file name: ")
    file = open(filename, 'r')
    for f in file:
        print(f.strip())
    file.close()
except FileNotFoundError:
    print("Error: The file",filename,"was not found.")