import random
word_list =["apple","mango","grapes","peach"]
lives = 6
output=  random.choice(word_list)
# print(output)

placeholder = ""
word_length = len(output)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"{lives}/6")
    guess = input("Guess the word: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display =""

    for letter in output:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+="_"

    print(display)

    if guess not in output:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
    
    if "_" not in display:
        game_over= True
        print("You Win.")