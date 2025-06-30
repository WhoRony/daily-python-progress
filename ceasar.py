alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar (original_text , shift_amount , encode_or_decode):
    # output_text = "This is my dummmy text"
    if encode_or_decode == "decode":
                shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position = alphabet.index(letter)+shift_amount
            output_text+=alphabet[shifted_position]
    print(f"Here is the encoded result:{output_text}")

should_countinue = True

while should_countinue:
    direction  = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    text = input("Type your message:").lower()
    shift = int(input("Type the shift number:"))

    ceasar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if restart == "no":
        should_countinue = False
        print("Goodbye")