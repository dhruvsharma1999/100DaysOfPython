alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

from D3_cipher_art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction =="decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {cipher_direction}d result: {end_text}")



#if user wants to restart the encryption by typing 'yes' or 'no'
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25

    caesar(start_text =text, shift_amount = shift, cipher_direction = direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")



# SKELETOL CODE


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount, direction_chose):
#     if direction_chose == "encode":
#         cipher = ""
#         for letters in plain_text:
#             position = alphabet.index(letters)
#             newPosition = position + shift_amount
#             newLetter = alphabet[newPosition]
#             cipher += newLetter
#         print(f"The encoded text is {cipher}")

#     elif direction_chose == "decode":
#         cipher_decode = ""
#         for letters in plain_text:
#             position_decode = alphabet.index(letters)
#             new_position_decode = position_decode - shift_amount
#             new_letter = alphabet[new_position_decode]
#             cipher_decode += new_letter
#         print(f"The decoded text is {cipher_decode}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"


    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


