import random

shapes = {"s": "✂", "p": "📄", "r": "🤘"}

def gameSystem():
    print("Welcome to Rock Paper Scissor game.\nChoose a shape by entering its initial.\nExample, r for Rock, s for Scissors and p for paper.\nGood luck!\n")
    playerID = input("Please enter your name: ").capitalize()
    print("")
    points = {playerID: 0, "Computer": 0}
    state = True

    while state:
        items = dict()
        playerShape = input("Choose a shape on the count of three 1, 2, 3: ")
        print("")

        if playerShape not in shapes:
            print("Please choose Paper (p), Scissors (s) or Rock(r).\n")
            continue

        computerShape = random.choice(list(shapes.keys()))
        items[playerShape], items[computerShape] = playerID, "Computer"
        print(f"{playerID}: {shapes[playerShape]}{' ' * 10}Computer: {shapes[computerShape]}\n")

        if playerShape == computerShape: print(f"Its a Withdraw\n\n{playerID}: {points[playerID]}{' ' * 11}Computer: {points['Computer']}\n")
        elif "r" not in items:
            points[items['s']] += 1
            print(f"{items['s']} gets point !!!\n\n{playerID}: {points[playerID]}{' ' * 11}Computer: {points['Computer']}\n")
        elif "p" not in items:
            points[items['r']] += 1
            print(f"{items['r']} gets point !!!\n\n{playerID}: {points[playerID]}{' ' * 11}Computer: {points['Computer']}\n")
        elif "s" not in items:
            points[items['p']] += 1
            print(f"{items['p']} gets point !!!\n\n{playerID}: {points[playerID]}{' ' * 11}Computer: {points['Computer']}\n")

        if 3 in points.values():
            print("#####################################################\n"
                f"#################### {list(points.keys())[list(points.values()).index(3)]} #######################\n"
                "#####################################################\n")
            state = False

    while True:
        answer = input("Do you wanna play again (y or n)?: ")
        print("")

        if answer == "y": gameSystem()
        elif answer == "n": exit()
        else: print("Please enter y or no\n")

if __name__ == '__main__':
    gameSystem()