import random
import time

def matches(): 
    hi = (input("hello, HUMAN. Please introduce yourself: "))
    time.sleep(0.5)
    print(f"well, {hi}.. ")
    time.sleep(1)
    print("You chose to play the game of matches with a powerful and dangerous machine.")
    time.sleep(0.5)
    print("There are 21 of them laying in front of you. Your goal is to make the machine take the last match.")
    print("You can only take 1,2,3 matches per move.")
    time.sleep(1)
    print(f"Good luck, {hi}")
    time.sleep(0.5)
    b = 0  
    a = 21

    while a != 1: 
        b = int(input(f"hom many matches do you take, {hi}?  "))
        if b > 3 or b <= 0:
            print("you can't take this amount of matches. Take from 1 to 3 ")
        else:
            a = a - b
            print(f"you took {b} matches. There are {a} matchs left. Your turn is over, now wait for the machine to make a move.")
            if a == 1:
                time.sleep(2)
                print(f"looks like you won {hi}! haven't seen that happen in the last trillion years. Here, take this choclate bar")
                break
            c = random.randint(1,3)
            a = a - c
            if a == 1:
                time.sleep(2)
                print(f"the machine took {c} matches. There is 1 match left.")
                print("oh. You lost. Prepare to be devoured :)")
                break
            else:
                time.sleep(2)
                print(f"the machine took {c} matches. There are {a} matches left. Your turn.")
                
    
            
            
matches()
