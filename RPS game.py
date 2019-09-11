#rock paper scissors game

#player is given three tries

#computer generates random try compares it to the three scenarios

#scisscors wins over paper
#rock wins over scissors
#paper wins over rock

#if same its draw
#player wins if they have more wins that the other

import random

def main():
    option = ["scissors","rock","paper"]
    player_win = 0
    player_lose = 0
    draw = True
    guess_no = 1
    guess=""
    correct = False 
    guess_count = False

    def no_try():
        while no_guess < 4:
            player_guess = str(input("Enter guess: "))
            comp_gen = random.choice(option)
            
            if player_guess == comp_gen:
                print(comp_gen + ", It's a draw")                
                draw = player_lose+1 and player_win+1
                
            elif player_guess =! comp_gen:
                if player_guess == 'scissors' and comp_gen == 'rock':
                    print( comp_gen + ", You Lose")
                    player_lose+1
                    
                elif player_guess == 'scissors' and comp_gen == 'paper':
                    print(comp_gen+", You win")
                    player_win+1
                    
                elif player_guess == 'rock' and comp_gen == 'scissors':
                    print(comp_gen + ", You win")
                    player_win+1

                elif player_guess == 'rock' and comp_gen == 'paper':
                    print(comp_gen + ", You lose")
                    player_lose+1

		elif player_guess == 'paper' and comp_gen == 'rock':
                    print(comp_gen + ", You lose")
                    player_lose+1

		elif player_guess == 'paper' and comp_gen == 'scissors':
                    print(comp_gen + ", You win")
                    player_win+1
                
            no_guess =+ 1

    def winner():
        if player_win + draw => player_lose:
            print ("You win, you got"+ player_win +"and the computer got "+player_lose)
