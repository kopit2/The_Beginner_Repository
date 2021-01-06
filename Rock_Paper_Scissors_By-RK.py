#Rock_Paper_Scissors_By_RK
##########################################
from random import shuffle
import random
##########################################
list_best_of = ["1", "3", "5"]
options = ["ROCK", "PAPER", "SCISSORS"]
shuffle(options)
player_score = 0
pc_score = 0
pc_option = random.choice(options)
best_of = 7
A = "ROCK"
B = "PAPER"
C = "SCISSORS"
best_of_choice = "2"
player_op = ""
##########################################
def op_shuf():
    shuffle(options)
    return options

##########################################
while best_of_choice not in list_best_of:
    print(pc_score , player_score)
    best_of_choice = input("DO YOU WANT TO PLAY BEST OF (1/3/5)?: ")
    if best_of_choice == "1":
        best_of = 1
    elif best_of_choice == "3":
        best_of = 2
    elif best_of_choice == "5":
        best_of = 3
    else:
        print("INVALID INPUT")
############################################
while pc_score != best_of and player_score != best_of:
    print("_______________________________________________________________________________________________")
    print(str("WE ARE PLAYING A BEST OF: " + str(best_of_choice)))
    print("SCORE BOARD - ""YOUR SCORE: " + str(player_score) + "   PC SCORE: " + str(pc_score))
    player_op = input("PLEASE CHOOSE (A/B/C):\nA.ROCK\nB.PAPER\nC.SCISSORS\nYOUR CHOICE: ").upper()
    op_shuf()
    if player_op == "A" and pc_option == A:
        print("PC CHOOSE: " + A)
        print("TIE!")
        op_shuf()
        pc_option = random.choice(options)
    elif player_op == "A" and pc_option == B:
        print("PC CHOOSE: " + B)
        print("YOU LOST THE ROUND :(")
        pc_score += 1
        op_shuf()
        pc_option = random.choice(options)
    elif player_op =="A" and pc_option == C:
        print("PC CHOOSE: " + C)
        print("YOU WON THE ROUND!!!")
        player_score += 1
        op_shuf()
        pc_option = random.choice(options)
    #################A
    if player_op == "B" and pc_option == B:
        print("PC CHOOSE: " + B)
        print("TIE!")
        op_shuf()
        pc_option = random.choice(options)
    elif player_op == "B" and pc_option == C:
        print("PC CHOOSE: " + C)
        print("YOU LOST THE ROUND :(")
        pc_score += 1
        op_shuf()
        pc_option = random.choice(options)
    elif player_op =="B" and pc_option == A:
        print("PC CHOOSE: " + A)
        print("YOU WON THE ROUND!!!")
        player_score += 1
        op_shuf()
        pc_option = random.choice(options)
    ###################B
    if player_op == "C" and pc_option == C:
        print("PC CHOOSE: " + C)
        print("TIE!")
        op_shuf()
        pc_option = random.choice(options)
    elif player_op == "C" and pc_option == A:
        print("PC CHOOSE: " + A)
        print("YOU LOST THE ROUND :(")
        pc_score += 1
        op_shuf()
        pc_option = random.choice(options)
    elif player_op =="C" and pc_option == B:
        print("PC CHOOSE: " + B)
        print("YOU WON THE ROUND!!!")
        player_score += 1
        op_shuf()
        pc_option = random.choice(options)
    ####################C
    elif player_op not in ["A", "B", "C"]:
        print("INVALID INPUT")
if pc_score > player_score:
    print("___________________________________________________________________________________________________________")
    print("YOU LOST TO THE PC YOU NOOB\nFINAL SCORE-BOARD:  YOUR SCORE: " + str(player_score) + "   PC SCORE: " + str(pc_score))
    print("___________________________________________________________________________________________________________")
else:
    print("___________________________________________________________________________________________________________")
    print("YOU WON!!!!! YOU ARE A LEGEND\nFINAL SCORE-BOARD:  YOUR SCORE: " + str(player_score) + "   PC SCORE: " + str(pc_score))
    print("___________________________________________________________________________________________________________")

