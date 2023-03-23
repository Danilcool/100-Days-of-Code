#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


starting_letter = open('Input/Letters/starting_letter.txt')
starting_letter_content = starting_letter.read()

with open('Input/Names/invited_names.txt', 'r') as name_list:

    for name in name_list:
        name = name.strip()

        finished_letter = open(f"Output/ReadyToSend/{name} invite letter.txt",'w')
        finished_letter.write(starting_letter_content.replace("[name]", f"{name}"))
        finished_letter.close()











