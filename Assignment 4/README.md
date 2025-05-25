## Task 1: Reading a File with Error Handling

For this task, I used a simple method to open the file and read its contents. I implemented a `for` loop to extract and print each line from the file.  
The entire process was wrapped inside a `try` block to handle errors gracefully. If the file does not exist, an appropriate message is displayed using the `except` block.

## Task 2: Writing and Appending to a File

In this task, I first opened the file in **write mode** to write the initial text.  
Then, I reopened the file in **append mode** to add more content on a **new line**.  
Without the newline (`\n`), the appended text would be added directly after the last character.  

Finally, I opened the file in **read mode** and printed its contents to the screen to verify the changes.
