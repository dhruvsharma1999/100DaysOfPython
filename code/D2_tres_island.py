print("Welcome to Tresure Island")
print("Welcome to Tresure Island. Your mission is to find the treasure.")

choice_1 = input("where do you want to go? left or right ?\n")

if choice_1 == "left":
    choice_2 = input("You have come to a lake. There is a island in middle of the lake. Type 'wait' to wait for boat. Type 'swim' to swim to the island: ")
    if choice_2 == "wait":
        choice_3 = input("You have arrived at the island, Which door you want to choose, Red, Blue, Yellow ?\n")
        if choice_3 == "red":
            print("game over")
        elif choice_3 == "blue":
            print("game Over")
        elif choice_3 == "yellow":
            print("YOU WON !")
        else:
            print("wrong door ! Game Over.")
    else:
        print("You got attacked by an angry shark. Game Over")   

 
        
else:
    print("You fell into a hole. Game Over.")
