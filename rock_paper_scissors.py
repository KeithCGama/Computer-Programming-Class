# call library for random numbers
from random import randrange

#Variable that holds the maximum number for the range
LIMIT = 4

#1st function: Ask user to choose weapon and dont return parameter
def Weapon_Choice():
    print("\nSELLECT YOUR WEAPON (1-3)")
    print("------------------------")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
#collect user input for choice, with in the range 1-3. Choce will be returned as an integer
    choice = int(input("Enter your Weapon: "))
    return choice

#2nd function: Opponets choice using random number with in range
def Opponents_weapon():
    return randrange(1, LIMIT)


#3rd function: Algerithem for winner
def Winner(Player_1, Player_2):
    #print()
    
    if Player_1 == Player_2:
        print("It's a tie!")

    elif Player_1 == 1 and Player_2 == 2:
        print("You lose, paper covers rock!")

    elif Player_1 == 2 and Player_2 == 1:
        print("You win, Paper covers Rock")

    elif Player_1 == 3 and Player_2 == 2:
         print("You win, Scissors cuts Rock")

    elif Player_1 == 2 and Player_2 == 3:
         print("You loose, Scissors cuts Rock")

    elif Player_1 == 3 and Player_2 == 1:
         print("You loose, Rock crushes Scissors!")

    elif Player_1 == 1 and Player_2 == 3:
        print("You win, Rock crushes Scissors!")

#main function
def main():
        #for boolen logic
        Play_again = "y"

        while Play_again.lower() == "y":
            Player1 = Weapon_Choice()
            Player2 = Opponents_weapon()
            Winner(Player1, Player2)
            Play_again = input("Want to play again (y/n): ")
            #print()

        print("Completed by, Keith Gama")
#call main
if __name__ == "__main__":
    main()
        

    

    
