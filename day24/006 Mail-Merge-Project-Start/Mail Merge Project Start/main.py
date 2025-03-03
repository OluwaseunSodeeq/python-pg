#TODO: Create a letter using starting_letter.txt 
print(f"Welcome to the Mail Merge Project")

new_letter =  ""


#for each name in invited_names.txt
invited_names = []
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
     # Read all lines from the file
    invited_names = file.readlines() 
     # Remove any leading/trailing whitespace from each line
    invited_names = [name.strip() for name in invited_names] 
    # print(invited_names)

    for invited_name in invited_names:
      with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
        contents=  file.read()
        new_letter = contents.replace("[name]", invited_name)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/{invited_name}.txt",mode="w") as file:
           file.write(new_letter)


#NOTE
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp