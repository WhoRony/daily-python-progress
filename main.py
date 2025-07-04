import random
# cards = [1,2,3,4,5,6,7,8,9,10,11]


#1.While game keep playing 
#2.While game keep drawing cards 
user_total_score = 0
user_card = []

computer_total_score=0
computer_card=[]


for i in range(2):
    # Generated random number will be between 1 to 1000 but different in every run.
    dealer = random.randint(1,11)
    user_card.append(dealer)
    user_total_score+=dealer

for j in range(1):
    computer_dealer = random.randint(1,11)
    computer_card.append(computer_dealer)
    computer_total_score+= computer_dealer
    

print(f"Your cards: {user_card}, current score: {user_total_score}\n computer current score:{computer_total_score}")

keep_playing = True

while keep_playing:
    add_more = input(f"Do you want to draw next card: Type 'y' or 'n': ").lower()

    if add_more == "y":
        user_card.append(dealer)
        print(user_card)
        user_total_score+=dealer
        print(user_total_score)

        computer_card.append(computer_dealer)
        print(computer_card)
        computer_total_score+=computer_dealer
        print(computer_total_score)
    elif add_more == "n":
        print(f"Your final hand: {user_card}, final score: {user_total_score}")
        print(f"Computer's final hand: {computer_card}, final score: {computer_total_score}")
    
        if user_total_score > computer_total_score:
            print("You won!")
        else:
            print("Computer Won!")

    if user_total_score == 21:
        print("You Won!")
    elif computer_total_score == 21:
        print("Computer Won!")
    elif user_total_score > 21:
        print(f"You reached! over 21 , Your current score: {user_total_score}\nYou lost!")
        keep_playing= False
    elif computer_total_score > 21:
        print(f"Computer reached! over 21 , Your current score: {user_total_score}\nYou Won!")
        keep_playing= False       


# MAKE A CLEAR LOGIC OF IF ELSE FOR REACHING EVERY EDGE CASE
