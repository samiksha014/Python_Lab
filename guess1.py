import random

def guess_the_number_and_win_prize():
	game_state = initialize()
	entry_fee , secret_number = game_state
	start_game(entry_fee , secret_number)
	
def initialize():
    entry_fee = int(input("Entry fee: "))
    secret_number = random.randint(1,100)
    return entry_fee , secret_number
    
def start_game(entry_fee, secret_number):
    attempts = 5
    for attempt in range(1,attempts+1):
        print("Guess the number")
        guess = int(input("Enter your guess: "))
        
        if guess == secret_number:
            print(f"Congratulations , you won! You guessed the number in {attempt} attempt.")
            prize = entry_fee * (6 - attempt)
            print(f"Your prize is ${prize}")
            return 
        else:
            num = (secret_number - guess)/secret_number
            
            if num > 0.6:
                print("Too small !! Try again!")
            elif 0.3 < num <= 0.6:
                print("Small!! Try again!")
            elif -0.3 < num <= 0.3:
                print("Large !! Try again!")
            else:
                print("Too large!! Try again!")
            
    print(f"Sorry, you have run out of attempts . The secret number is {secret_number}")

guess_the_number_and_win_prize()

    
    
    

    
    
    
        
	
	
	
