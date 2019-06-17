import os
import random
import unittest

decks = input("Enter number of decks to use: ")

# user chooses number of decks of cards to use
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

# initialize scores
wins = 0
losses = 0
money = 1000
quit = False

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    global wins
    global losses
    global money
    again = input("Do you want to play again? (Y/N) : ").lower()
    while (again != 'y') and (again != 'n'):
        print('Wrong input!')
        again = input("Do you want to play again? (Y/N) : ").lower()
        
        
    if again == "y":
        wins = 0
        losses = 0
        money = 1000
        #dealer_hand = []
        #player_hand = []
        #deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
        
    elif again == "n":
        print("Bye!")
        exit()

    elif again != "y" or again !="n":
        print("You have to choose between 'y' for yes or 'n' for no")
        play_again()
    

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()
    print ("The dealers hand is  " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    
def print_score(wins, losses, money):
   
    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n   \033[1;32;40mMONEY:  \033[1;37;40m%s" % (wins, losses, money))
    print("-"*30+"\n")
    


def blackjack_dealer(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("The player got a blackjack! You lost!\n")
        losses += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("You got a blackhack! You won!\n")
        wins += 1
        play_again()



def score(dealer_hand, player_hand, bet):
        # score function now updates to global win/loss variables
        global wins
        global losses
        global money
        if total(player_hand) == 21:
           
            print ("Congratulations! You got a Blackjack!\n")
            wins += 1
            money += int(bet)
        elif total(dealer_hand) == 21:
            
            print ("Sorry, you lose. The dealer got a blackjack.\n")
            losses += 1
            money -= int(bet)
        elif total(player_hand) > 21:
            
            print ("Sorry. You busted. You lose.\n")
            losses += 1
            money -= int(bet)
        elif total(dealer_hand) > 21:
            
            print ("Dealer busts. You win!\n")
            wins += 1
            money += int(bet)
        elif total(player_hand) < total(dealer_hand):
            
            print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
            losses += 1
            money -= int(bet)
        elif total(player_hand) > total(dealer_hand):
            
            print ("Congratulations. Your score is higher than the dealer. You win\n")
            wins += 1
            money += int(bet)

def score_dealer(dealer_hand, player_hand):
        # score function now updates to global win/loss variables
        global wins
        global losses
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("The player got a BLACKJACK! You lost!\n")
            losses += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("You got a BLACKJACK! You won!\n")
            wins += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("The player busted. You win!\n")
            wins += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("You bust! You lost!\n")
            losses += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Your score is higher than the players. You win!\n")
            wins += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Your score is lower than the players. You lost!\n")
            losses += 1

def game():
    global wins
    global losses
    choice = 0
    userchoice = 0
    aichoice = ["h", "s"]
    clear()
    
    userchoice = input("Do you want to be a [D]ealer or a [P]layer: ").lower()
    while (userchoice != 'd') and (userchoice != 'p'):
        print('Wrong input!')
        userchoice = input("Please enter 'p' for 'Player' or 'd' for 'Dealer': ").lower()

    if userchoice == 'd':
            quit = False

            print("-"*30+"\n")
            print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
            print("-"*30+"\n")
            dealer_hand = deal(deck)
            player_hand = deal(deck)
            print ("Your hand is " + str(dealer_hand[0]))
            print ("The players hand is " + str(player_hand) + " for a total of " + str(total(player_hand)))
            blackjack_dealer(dealer_hand, player_hand)
            
         

            while not quit:
                print ("Now the player will choose...")
                print ("-"*30+"\n")
                choice = random.choice(aichoice)
                if choice == 'h':
                    print('The players choice is to hit!')
                    hit(player_hand)
                    print("The players hand is " + str(player_hand))
                    print("The players hand total is " + str(total(player_hand)))
                    print("\n")
                    if total(player_hand)>21:
                        print('You win, the player busted!')
                        print("The players hand total exceeded 21")
                        print ("-"*30+"\n")
                        wins += 1
                        play_again()

                elif choice == 's':
                    print ("The players choice is to stand")
                    print ("-"*30+"\n")
                    while total(dealer_hand)<17:
                        hit(dealer_hand)
                        print(dealer_hand)
                        if total(dealer_hand)>21:
                            print('You busted, the player wins!')
                            print("\n")
                            losses += 1
                            play_again()
                    
                    
                elif choice == 'q':
                    print('The game ended, the player left the table!')
                    quit = True
                    exit()

                


    if userchoice == 'p':
        
        global money
        bet = 0
        
        
        while money > 0:
            print_score(wins,losses,money)
            
            quit = False
            bet_status = False
            
            while not bet_status:
                bet = input("Choose your bet, must be lower than " + str(money) + "\n")
                if bet.isdigit() is False:
                    print("The value you enter must be a number only!")
                
                elif int(bet) <= money:
                    bet_status = True
                elif int(bet) > money:
                    print("Wrong input!")
                
            
            dealer_hand = deal(deck)
            player_hand = deal(deck)
            print ("The dealer is showing a " + str(dealer_hand[0]))
            print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
            
            
            
            while not quit:
                if total(player_hand) == 21:
                    print_results(dealer_hand, player_hand)
                    print ("Congratulations! You got a Blackjack!\n")
                    wins += 1
                    money +=int(bet) 
                    quit = True
                   
                        
                elif total(dealer_hand) == 21:
                    print_results(dealer_hand, player_hand)
                    print ("Sorry, you lose. The dealer got a blackjack.\n")
                    losses += 1
                    money -=int(bet)
                    quit = True
                
                elif total(dealer_hand) and total(player_hand) !=21:
                    choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                    print("-"*30)
                    while (choice != 'h') and (choice != 's') and (choice != 'q'):
                        print('Wrong input!')
                        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                        
                    
                    if choice == 'h':
                        print("Your choice was to hit\n")
                        hit(player_hand)
                        print("Your hand is: " + str(player_hand))
                        print("The total value of your hand is: " + str(total(player_hand)))
                        print("-"*30)
                        if total(player_hand)>21:
                            print('You busted!')
                            print('Dealer wins!')
                            print("-"*30)
                            losses += 1
                            money = money - int(bet)
                            quit = True
                        elif total(player_hand)==21:
                            print('Congratulations! You got a BLACKJACK!')
                            print("-"*30)
                            wins +=1
                            money = money + int(bet)
                            quit = True
                                
                    elif choice=='s':
                        print("Your choice was to stand")
                        print("-"*30)
                        while total(dealer_hand)<17:
                            hit(dealer_hand)
                            
                        print("The dealers hand is: " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
                        print("Your hand is: " + str(player_hand) + " for a total of " + str(total(player_hand)))
                        print("-"*30)            
                        score(dealer_hand,player_hand,bet)
                        quit = True

                    elif choice == "q":
                        print("Your choice was to quit\n")
                        print("Bye!")
                        quit=True
                        exit()
        print("You are out of credits! You are kicked out of the table!")
        play_again()


class TestMethods(unittest.TestCase):
    
    def test_totalhand(self):
        self.assertEqual(total(['J','A']), 19)
        
    def test_totalhand2(self):
        self.assertEqual(total(['J','A']), 21)



if __name__ == "__main__":
   #unittest.main(verbosity=3)
   game()
   