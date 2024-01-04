import art 
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs and decrypt function as caesar.
#TODO-1.1: Combine the encrypt and decrypt function into a single function called caesar().
def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
             position=alphabet.index(char)
             new_position=position+shift_amount
             end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d result: {end_text}")
def encrypt(plain_text,shift_amount):
    cipher_text=" " 
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        new_letter=alphabet[new_position]
    print(f"The encoded text is:{cipher_text}")

#TODO-2: Inside the 'encrypt' function, shift each letter of the text forward in the alphabet by the shift amount and print the encrypted text

#caesar(start_text=text, shift_amount=shift,cipher_direction=direction)
#TODO-3: Call the encrypt function and pass the user inputs. You should be able to test the code and encrypt a message.
    #3.1: 
    
#TODO-4: Create a different function called decrypt that takes the text and shift as inputs
def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text: #letter=k
        position=alphabet.index(letter)
        new_position=position-shift_amount
        cipher_text+=alphabet[new_position]
    print(f"The decoded text is {cipher_text}")
wanna_end= False
while not wanna_end:
    what_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text=input("Type your message:\n")
    shift=int(input("Enter shift key:\n"))
    if what_to_do=="encrypt":
        encrypt(plain_text=text,shift_amount=shift)
    elif what_to_do=="decrypt":
        decrypt(cipher_text=text,shift_amount=shift)
    print(f"The decoded text is:{text}")
    play_again=input("Type 'yes' to continue and type 'no' to exit" )
    if play_again=='no':
        wanna_end=True
        print("Bye")