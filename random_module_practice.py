import random
import time


def russian_rulette1(full_simulation=True):
    result = random.randint(0, 1)
    if full_simulation:
        print("барабан крутиться")
        time.sleep(2)
        print("натиснення на курок")
    if result == 0:
        if full_simulation:
            print("сдох.")
        return False
    else:
        if full_simulation:
            print("вижив!")
        return True


# russian_rulette1()


def test1(N=100000):
    result_zeros = 0
    result_ones = 0
    for i in range(N):
        if not russian_rulette1(full_simulation=False):
            result_zeros += 1
        else:
            result_ones += 1
    percent_alive = round((result_ones / N) * 100)
    percent_dead = round((result_zeros / N) * 100)
    print(
        f"ти сдох {result_zeros} разів з {N} ігор. Ти вижив {result_ones} разів з {N} ігор. Ймовірність смерті - {percent_dead}% , Ймовірність виживання - {percent_alive}% ;"
    )


# for i in range(60):
#    test1(N=100)
# russian_rulette1()


def russian_rulette3():
    from random import randrange

    people_playing = int(input("скільки людей грає?"))
    queue = list(range(people_playing))
    your_index = int(input("який ти по черзі?"))
    queue[your_index] = "ME"

    while len(queue) != 1:
        baraban = [0] * 6
        baraban[randrange(0, 6)] = 1

        for i in range(len(queue)):
            if queue[i] == "ME":
                if baraban[i] == 0:
                    print("You're alive")
                else:
                    print("You're dead")
                    queue.pop(i)
                    return
            else:
                if baraban[i] == 0:
                    print(f" the player {queue[i]} is alive")
                else:
                    print(f" the player {queue[i]} is dead")
                    queue.pop(i)
                    break


russian_rulette3()


import random


def kubiki():
    cube_a = random.randrange(1, 6)
    cube_b = random.randrange(1, 6)
    result = cube_a + cube_b
    print("the cube is rolling...")
    print("Behold!")
    if result > 7:
        print(f"{result} - the score is too big, you only get 1 $")
    elif result < 7:
        print(f"{result} - the score is too small, you only get 1 $")
    elif result == 7:
        print("You got 7! The biggest prize is yours. +4 $ ")


# kubiki()
