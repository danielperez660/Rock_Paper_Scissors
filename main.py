import random


def m():
    initm = input("Want to play Rock, Paper, Scissors?(Y/N): ")

    if initm.lower() == 'y':
        return True
    elif initm.lower() == 'n':
        print("Bye!")
        exit(True)
    else:
        return False


def replay():
    initr = input("Want to play Rock, Paper, Scissors?(Y/N): ")

    if initr.lower() == 'y':
        rps()
    elif initr.lower() == 'n':
        print("Bye!")
        exit(True)
    else:
        print("INVALID INPUT")
        replay()


def rps():
    lose = {"s": "r", "p": "s", "r": "p"}
    comp = random.choice(["r", "s", "p"])
    user = input("Rock, Paper or Scissors?(R,P,S): ")

    if comp == lose[user.lower()]:
        print("You played: ", user, "\nComputer played: ", comp)
        print("You have lost!")
        print()
        replay()
    elif comp == user.lower():
        print("You played: ", user, "\nComputer played: ", comp)
        print("You have drawn!")
        print()
        replay()
    elif lose[comp] == user:
        print("You played: ", user, "\nComputer played: ", comp)
        print("You have won!")
        print()
        replay()
    else:
        print("INVALID INPUT")
        print()
        rps()


def init():
    if m():
        rps()
    else:
        print("INPUT INVALID")
    init()


init()
