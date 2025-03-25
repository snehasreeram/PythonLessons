alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Cease Cipher:

def cipher(direction, text, shift):
    text_list = list(text)
    result=[]

    if direction=='decode':
        shift = -shift

    for i in text_list:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index+shift) % len(alphabet) #modulo ensures new_index is always within [0,25]
            result += alphabet[new_index]
        else:
            result += i

    final_result=''.join(result)
    print(f"Your {direction}d phrase: {final_result}")

game_on = True
while game_on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ('encode', 'decode'):
        raise ValueError("Invalid mode! Use 'encode' or 'decode'.")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(direction, text, shift)

    go_again = input("Would you like to go again? Y/N: ").lower()
    if go_again == 'y':
        game_on=True
    else:
        game_on = False