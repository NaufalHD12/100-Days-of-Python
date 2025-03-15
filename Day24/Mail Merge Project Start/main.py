#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
# Buka dan baca template surat
with open("Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()  # Read the entire file as a string

# Buka dan baca daftar nama
with open("Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()  # Read names and split into a list
    
for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    output_path=f"Day24\Mail Merge Project Start\Output\ReadyToSend/letterfor{name}"
    
    with open(output_path, mode="w") as ready_to_send:
        ready_to_send.write(personalized_letter)