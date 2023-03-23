alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'," "]


def encrypt(plain_text,plain_shift):
    final = ""
    plain_shift = plain_shift % 26
    for letter in plain_text:
        x = alphabet.index(letter)
        new_position = x + plain_shift
        if new_position > 26:
            new_position -= 27
        final += alphabet[new_position]
    print(final)

def uncode(coded_text,shift):
    uncoded_word = ""
    shift = shift % 26
    for letter in coded_text:
        text_postion = alphabet.index(letter)
        new_position = text_postion - shift

        uncoded_word += alphabet[new_position]
    print(uncoded_word)


should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":

        encrypt(text, shift)

    elif direction == "decode":

        uncode(text, shift)
    restart = input("Do you wonna Restart: (yes or no)").lower()
    if restart == "no":
        should_continue = False

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

