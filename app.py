import os
import random
import unittest

#The deck is a list consisting of numbers that represents the type of cards you are going to draw
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

#Here i initialize the scores so i can modify them globally
wins = 0
losses = 0
money = 1000
quit = False

#This method  takes a card out of the deck and puts it into the hand of either the player or the dealer 
def deal(deck):
    hand = []
    #Used this for loop in order to put 2 cards in the hand of the dealer and the player 
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

#This method tests if the user wants to play the game again 
def play_again():
    #Initializing the values with global to make sure they will be modified globally
    global wins
    global losses
    global money
    
    #Here i use the input() method to take the input of the user 
    #After that i make use of the while loop in order to make sure that the user can enter either 'y'  for yer or 'n' for no
    again = input("Do you want to play again? (Y/N) : ").lower()
    while (again != 'y') and (again != 'n'):
        print('Wrong input!')
        again = input("Do you want to play again? (Y/N) : ").lower()
        
    #This if statement resets the values of wins, losses and money to be ready for a new game
    #Also makes sure that the dealer hand and the player hand is empty
    #Choosing 'y' also invokes the game method in order to play the game again 
    if again == "y":
        wins = 0
        losses = 0
        money = 1000
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    #If the player chooses n the program will quit
    elif again == "n":
        print("Bye!")
        exit()

    
#This method calculates the total of a hand, converting the the cards into values 
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
#This method takes a value from the deck listing represting a card and puts it into the hand list representing the hand of either the player or the dealer
def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand
#Clears the terminal of output
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')
        
#This method prints the hand and the value of that respective hand of both the dealer and the player
#It takes the dealer_hand and the player_hand lists as arguments 
#It makes use of the total() method in order to return the value of the 
def print_results(dealer_hand, player_hand):
    clear()
    print ("The dealers hand is  " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

#This method takes the value of wins, losses and money as arguments and prints out the statistics based on those values 
#It makes use of string interpolation formating
def print_score(wins, losses, money):
   
    print("\n                   STATS\n")
    print("-"*46+"\n")
    print(f"    \033[1;32;40mWINS:  \033[1;37;40m{wins}   \033[1;31;40mLOSSES:  \033[1;37;40m{losses}   \033[1;35;40mMONEY:  \033[1;37;40m{money}$\n" )
    print("-"*46+"\n")
    

#This method also takes the dealer hand and player hand lists and the calculates if either of them got a blackjack
#The if statements are using the total method in order to compare the value of the hand to 21 
def blackjack_dealer(dealer_hand, player_hand):
    global wins
    global losses
    #If it they pass the black jack test the wins and losses are update accordingly and the play_again() method is invoked
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


#This method uses the lists of dealer and player , and also the bet variable as an argument 
#Based on the value of the hand it calculates who wins that specific round 
#Adjusts the money variable in accordance with the bet that is an input from the user 
def score(dealer_hand, player_hand, bet):
        
        global wins
        global losses
        global money
        
        #Multiple if statements will use the total() method to compare the value of the hand with various values in order to determine 
        #the outcome of a round
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

#This method is very similar to the score method  used for the player
def score_dealer(dealer_hand, player_hand):
        
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
            
#The game method incorporates all of the methods above to deliver the actual game
def game():
    #I initialize the wins and losses values globally in order to be modified inside the if statements below
    global wins
    global losses
    #The choice attribute will be used to retain the input of the player through a round, if the stays, hits or quits the table
    choice = 0
    #The userchoice is used to allow the user to choose if he wants to play as a dealer or as a player 
    userchoice = 0
    #The aichoice is a list and will be used to randomly select a choice for the 'ai' when you play in dealer mode 
    aichoice = ["h", "s"]
    
    #Taking the userinput and making sure he can choose only specific values
    userchoice = input("Do you want to be a [D]ealer or a [P]layer: ").lower()
    while (userchoice != 'd') and (userchoice != 'p'):
        print('Wrong input!')
        userchoice = input("Please enter 'p' for 'Player' or 'd' for 'Dealer': ").lower()
    clear()
    
    #If the player chooses to go in dealer mode the following sequence will happen
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

                

    #If the user chooses player mode the following sequence will take place 
    if userchoice == 'p':
        #I initialize the money value globally in order to be modified across all of the program
        global money
        bet = 0
        
        #This while loop will run until the money value drops to 0,after that the game ends
    
        while money > 0:
            #After each round i print the stats using the wins, losses and money attributes
            print_score(wins,losses,money)
            #I initialize the boolean quit to be use for the while loop that will take care of the round progression
            quit = False
            #I initialize the boolen bet_status in order to be used to test the input of the user
            bet_status = False
            #This while loop makes sure that the user will input a bet that is a number and is lower than total amount of money he has
            while not bet_status:
                bet = input("Choose your bet, must be lower than " + str(money) + "\n")
                if bet.isdigit() is False:
                    print("The value you enter must be a number only!")
                
                elif int(bet) <= money:
                    bet_status = True
                elif int(bet) > money:
                    print("Wrong input!")
                
            #The dealers hand and the players hand are dealt using the deal() method
            dealer_hand = deal(deck)
            player_hand = deal(deck)
            
            #Printing the first card of the dealer and the hand of the player
            print ("The dealer is showing a " + str(dealer_hand[0]))
            print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
            
            
            #The while loop runs while the value of quit is False 
            #If one of the if statements condition is met than the value of quit is modified to True and the round is finished
            while not quit:
                
                #The first 3 if statements will test if either the player or the dealer will get a blackjack in the first round
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
                #If a blackjack is not present in the first hand than the game will continue and the player is greeted with another choice
                elif total(dealer_hand) and total(player_hand) !=21:
                    #The player need to choose if he want to hit stand or quit based on the hand he got
                    choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                    print("-"*30)
                    #This while loop makes sure that he user can't break the program by inputing a bad value 
                    while (choice != 'h') and (choice != 's') and (choice != 'q'):
                        print('Wrong input!')
                        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                        
                    #A couple of nested if conditions will determine the output of the round
                    #Each user choice will modifiy the game accordingly
                    
                    if choice == 'h':
                        print("Your choice was to hit\n")
                        #If the choose to hit the will receive another card using the hit() method
                        hit(player_hand)
                        print("Your hand is: " + str(player_hand))
                        print("The total value of your hand is: " + str(total(player_hand)))
                        print("-"*30)
                        #If the valuer of the hand exceeds 21 the player will loose the round and the bet will be deducted from his money
                        if total(player_hand)>21:
                            print('You busted!')
                            print('Dealer wins!')
                            print("-"*30)
                            losses += 1
                            money = money - int(bet)
                            quit = True
                        #If the value is 21 after a hit he gets a blackjack and wins , gaining the bet 
                        elif total(player_hand)==21:
                            print('Congratulations! You got a BLACKJACK!')
                            print("-"*30)
                            wins +=1
                            money = money + int(bet)
                            quit = True
                                
                    elif choice=='s':
                        print("Your choice was to stand")
                        print("-"*30)
                        #When he chooses to stand the dealer will gain cards until he exceeds 17
                        while total(dealer_hand)<17:
                            hit(dealer_hand)
                            
                        print("The dealers hand is: " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
                        print("Your hand is: " + str(player_hand) + " for a total of " + str(total(player_hand)))
                        print("-"*30)  
                        #After the condition of the dealer is met we invoke the score() method to determine who won the round          
                        score(dealer_hand,player_hand,bet)
                        quit = True

                    elif choice == "q":
                        print("Your choice was to quit\n")
                        print("Bye!")
                        quit=True
                        exit()
        #If the while loop condition is met the player will be greeted with the following message 
        print("You are out of credits! You are kicked out of the table!")
        play_again()

#I used testing in order to test if the total() method works properly
class TestMethods(unittest.TestCase):
    #I firstly test what the total() method will return if the player has a hand consisting in a 'j' and an ace, the corect value should be 21
    def test_totalhand(self):
        self.assertEqual(total(['J','A']), 19)
        
    def test_totalhand2(self):
        self.assertEqual(total(['J','A']), 21)



if __name__ == "__main__":
   #unittest.main(verbosity=3)
   game()
   