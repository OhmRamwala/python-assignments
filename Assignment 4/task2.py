# Task 2: Write and Append Data to a File

file = open('output.txt','w')
text=input("Enter text to write to the file:")
file.write(text)
print("Data Successfully written to output.txt")
file.close()

file = open('output.txt','a')
text_to_append = input("Enter additional text to append:")
file.write("\n"+text_to_append)
file.close()
print("Data Successfully appended to output.txt")

print("Final content of output.txt:")
file = open('output.txt','r')
print(file.read())
file.close()