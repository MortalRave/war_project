
from deck import *
from table import *
import os

m = True
while m:
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    print("-------\\\\\\\--------------------////------////\\\\\\\---------||||||||||||||--------")
    print("--------\\\\\\\------------------////------////--\\\\\\\--------||||||----|||||-------")
    print("---------\\\\\\\----////\\\\\\\----////------////||||\\\\\\\-------||||||||||||||--------")
    print("----------\\\\\\\--////--\\\\\\\--////------////------\\\\\\\------||||||----\\\\\\\--------")
    print("-----------\\\\\\\////----\\\\\\\////------////--------\\\\\\\-----||||||-----\\\\\\\-------")
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------\n\n\n")
    print("=======================")
    print("         MENU")
    print("=======================")
    print("1. START GAME")
    print("2. HOW TO PLAY")
    print("3. HISTORY")
    print("4. EXIT")
    print("=======================\n")


    def play():
        # Clearing screen
        os.system('cls||clear')

        # Preparing cards to play
        full_deck = Table([spades1,spades2,spades3,spades4,spades5,spades6,spades7,spades8,spades9,spades10,spadesj,spadesq,spadesk,spadesa,
                    hearts1,hearts2,hearts3,hearts4,hearts5,hearts6,hearts7,hearts8,hearts9,hearts10,heartsj,heartsq,heartsk,heartsa,
                    clubs1,clubs2,clubs3,clubs4,clubs5,clubs6,clubs7,clubs8,clubs9,clubs10,clubsj,clubsq,clubsk,clubsa,
                    diamonds1,diamonds2,diamonds3,diamonds4,diamonds5,diamonds6,diamonds7,diamonds8,diamonds9,diamonds10,diamondsj,diamondsq,diamondsk,diamondsa])
        full_deck.shuffle_deck()
        player1,player2 = full_deck.deal_the_cards([],[])
        # Game
        s = 0
        while len(player1) != 0 and len(player2) !=0:
            s+=1
            print("PLAYER 2")
            print(f"CARDS: {len(player2)}")
            print(player2[0].image)
            print("====================")
            a = input("Click 'ENTER' to pull a card")
            print ("\033[A                             \033[A")     # Delete last line in the screen
            print(player1[0].image)
            print(f"CARDS: {len(player1)}")
            print("PLAYER 1")
            # Player 1 won
            if player1[0].value > player2[0].value:
                player1.append(player2[0])
                player1.append(player1[0])
                player1.pop(0)
                player2.pop(0)
                a = input("\n\nYou won!\nClick 'ENTER' to continue or type 'Q' to quit.\n")
                if a == 'Q':
                    exit()
            # Player 2 won
            elif player1[0].value < player2[0].value:
                player2.append(player1[0])
                player2.append(player2[0])
                player1.pop(0)
                player2.pop(0)
                a = input("\n\nYou lost!\nClick 'ENTER' to continue or type 'Q' to quit.\n")
                if a == 'Q':
                    exit()
            #DRAW
            else:
                a = input("IT'S A WAR!\n\nClick 'ENTER' to continue or type 'Q' to quit.\n")
                # Clearing screen
                os.system('cls||clear')
                war_deck = []
                war = True
                while war:
                    a = input("First card blind...\n\nClick 'ENTER' to continue or type 'Q' to quit.\n")
                    if a == 'Q':
                        exit()

                    # Clearing screen
                    os.system('cls||clear')

                    # Back of cards
                    print("PLAYER 2")
                    print(f"CARDS: {len(player2)}")
                    print(cardsback.image)
                    print("====================")
                    print(cardsback.image)
                    print(f"CARDS: {len(player1)}")
                    print("PLAYER 1")
                    a = input("\n\nClick 'ENTER' to continue or type 'Q' to quit.\n")

                    # Clearing screen
                    os.system('cls||clear')

                    war_deck.append(player1[0])
                    player1.pop(0)
                    if len(player1) == 0:
                        break
                    war_deck.append(player2[0])
                    player2.pop(0)
                    if len(player2) == 0:
                        break
                    war_deck.append(player1[0])
                    player2.pop(0)
                    if len(player1) == 0:
                        break
                    war_deck.append(player2[0])
                    player2.pop(0)
                    if len(player2) == 0:
                        break

                    print("PLAYER 2")
                    print(f"CARDS: {len(player2)}")
                    print(player2[0].image)
                    print("====================")
                    a = input("Click 'ENTER' to pull a card")
                    print ("\033[A                             \033[A")     # Delete last line in the screen
                    print(player1[0].image)
                    print(f"CARDS: {len(player1)}")
                    print("PLAYER 1")

                    if player1[0].value > player2[0].value:
                        player1 += war_deck
                        player1.append(player2[0])
                        player1.append(player1[0])
                        player1.pop(0)
                        player2.pop(0)
                        war = False
                        a = input("\n\nYou won WAR!\nClick 'ENTER' to continue or type 'Q' to quit.\n")
                        if a == 'Q':
                            exit()
                    elif player1[0].value < player2[0].value:
                        player2 += war_deck
                        player2.append(player1[0])
                        player2.append(player2[0])
                        player1.pop(0)
                        player2.pop(0)
                        war = False
                        a = input("\n\nYou lost WAR!\nClick 'ENTER' to continue or type 'Q' to quit.\n")
                        if a == 'Q':
                            exit()

                        

            # Clearing screen
            os.system('cls||clear')   




        if len(player1) == 0:
            print("You LOSE")
            a = input("Click 'ENTER' to continue...")
            print ("\033[A                             \033[A")     # Delete last line in the screen
            name = input("Insert your name: ")
            while len(name) == 0:
                name = input("Insert your name: ")
            filepath = "history.txt"
            f = open(filepath, "r+")
            f.read()
            f.write(f"\n{name} - {s} moves - DEFEAT")
            # Clearing screen
            os.system('cls||clear')
            print(f"You lost in {s} moves")
            a = input("Click 'ENTER' to continue...")
        elif len(player2)==0:
            print("You WIN!\n")
            a = input("Click 'ENTER' to continue...")
            print ("\033[A                             \033[A")     # Delete last line in the screen
            name = input("Insert your name: ")
            while len(name) == 0:
                name = input("Insert your name: ")
            filepath = "history.txt"
            f = open(filepath, "r+")
            f.read()
            f.write(f"\n{name} - {s} moves - VICTORY")
            # Clearing screen
            os.system('cls||clear')
            print(f"You won in {s} moves")
            a = input("Click 'ENTER' to continue...")
        else:
            print("?")

        # Clearing screen
        os.system('cls||clear')
        
    def rules():
        # Clearing screen
        os.system('cls||clear')
        print("=================================================================================================================")
        print("The goal is to be the first player to win all 52 cards\n")
        print("Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, \nface down, on the bottom of his stack.\n")
        print("If the cards are the same rank, it is War. Each player turns up one card face down and one card face up. \nThe player with the higher cards takes both piles (six cards). If the turned-up cards are again the same rank, \neach player places another card face down and turns another card face up. \nThe player with the higher card takes all 10 cards, and so on.")

        a = input("\n\nClick 'ENTER' to continue or type 'Q' to quit.")
        if a == 'Q':
            exit()
        # Clearing screen
        os.system('cls||clear')

    def history():
        # Clearing screen
        os.system('cls||clear')
        filepath = "history.txt"
        f = open(filepath, "r")
        print(f.read())

        a = input("\n\nClick 'ENTER' to continue or type 'Q' to quit.")
        if a == 'Q':
            exit()
        # Clearing screen
        os.system('cls||clear')


    choice = input()
    if choice == '1':
        play()
    elif choice == '2':
        rules()
    elif choice == '3':
        history()
    elif choice == '4':
        print("Thanks for playing!")
        exit()    
