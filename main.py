import random

player1name = input("What is Player 1's name?")
player1totalscore = 0
turnscore = 0
rollscore = 0
player2name = input("What is Player 2's name?")
player2totalscore = 0
playernameturn = player1name

dice1state = "unlocked"
dice2state = "unlocked"
dice3state = "unlocked"
dice4state = "unlocked"
dice5state = "unlocked"
dice6state = "unlocked"

winner = False

while(winner == False):
    gamestate = "pending"

    while (gamestate == "pending"):

        gamestate = "pending"
        print("It is ",playernameturn,"'s turn!")
        print("Turn Score:",turnscore)
        turndecision = "reset"
        while (turndecision != "roll" and turndecision != "end"):
            turndecision = input("Enter ROLL to roll or END to end your turn")
        if(turndecision == "roll"):
            if dice1state == "unlocked":
                dice1 = random.randint(1,6)
            if dice2state == "unlocked":
                dice2 = random.randint(1,6)
            if dice3state == "unlocked":
                dice3 = random.randint(1,6)
            if dice4state == "unlocked":
                dice4 = random.randint(1,6)
            if dice5state == "unlocked":
                dice5 = random.randint(1,6)
            if dice6state == "unlocked":
                dice6 = random.randint(1,6)

            print("Dice 1: [",dice1,"] - ",dice1state)
            print("Dice 2: [",dice2,"] - ",dice2state)
            print("Dice 3: [",dice3,"] - ",dice3state)
            print("Dice 4: [",dice4,"] - ",dice4state)
            print("Dice 5: [",dice5,"] - ",dice5state)
            print("Dice 6: [",dice6,"] - ",dice6state)
        
            keepdicenumbers = str(input('Which Dice Do You Want To Keep? Enter The Dice Numbers. ("bust" to go bust)'))
        
        if keepdicenumbers == "bust":
            turndecision = "end"
            turnscore = 0
            rollscore = 0
            dice1state = "unlocked"
            dice2state = "unlocked"
            dice3state = "unlocked"
            dice4state = "unlocked"
            dice5state = "unlocked"
            dice6state = "unlocked"

        if keepdicenumbers.find("1") != -1:
            dice1state = "locked"
        if keepdicenumbers.find("2") != -1:
            dice2state = "locked"
        if keepdicenumbers.find("3") != -1:
            dice3state = "locked"
        if keepdicenumbers.find("4") != -1:
            dice4state = "locked"
        if keepdicenumbers.find("5") != -1:
            dice5state = "locked"
        if keepdicenumbers.find("6") != -1:
            dice6state = "locked"
        if keepdicenumbers.find("end") == -1:
            gamestate = "ended"
        if (dice1state == "locked" and dice2state == "locked" and dice3state == "locked" and dice4state == "locked" and dice5state == "locked" and dice6state == "locked"):
            dice1state = "unlocked"
            dice2state = "unlocked"
            dice3state = "unlocked"
            dice4state = "unlocked"
            dice5state = "unlocked"
            dice6state = "unlocked"
        if(keepdicenumbers != "bust" and turndecision != "end"):
            while True:
                try:
                    rollscore = int(input("How many points did you get on this roll?"))
                    break
                except:
                    print("That's not a valid option")
                
            turnscore += rollscore

        if turndecision == "end": 
            if playernameturn == player1name:
                player1totalscore += turnscore
            if playernameturn == player2name:
                player2totalscore += turnscore
            dice1state = "unlocked"
            dice2state = "unlocked"
            dice3state = "unlocked"
            dice4state = "unlocked"
            dice5state = "unlocked"
            dice6state = "unlocked"
            if playernameturn == player2name:
                playernameturn = player1name
            else:
                playernameturn = player2name
            gamestate = "ended"
            print(player1name,":",player1totalscore,"points ",player2name,":",player2totalscore,"points")
            turnscore = 0
            rollscore = 0
        if player1totalscore >= 10000:
            print(player1name," WINS!")
            gamestate = "winner"
            winner = True
        if player2totalscore >= 10000:
            print(player2name," WINS!")
            gamestate = "winner"
            winner = True



        


            

