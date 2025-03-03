comments =  '''
    file  = open("my_file.txt")
    contents = file.read()

    print(contents)
    file.close()

    u dont have to manually close the file in the below approach
    To overwrite the initial content in the file
    with open("my_file.txt", mode="w") as file:

    To append to the initial content
    with open("my_file.txt", mode="a") as file:

    with open("my_file.txt", mode="a") as file:
        contents = file.read()
        print(contents)
'''
print("hello index")
with open("my_file.txt", mode="a") as file:
   file.write("\nNew text is added")

with open("new-file.txt", mode="w") as file:
   file.write("hello Oluwaseun \n I am new file")








