import random
import csv


def generator(file):
    with open (file) as file:
        reader = csv.reader(file)
        random_row = random.choice(list(reader))

    parsed = random_row[0].split("|")
    return parsed

def main():
    while True:
        print("Monopoly card generator")
        print("Press 1 for chance")
        print("Press 2 for community chest")
        print("Press 3 to quit")
        user_input = input("Action: ")
        if user_input == "1":
            card = generator("chance.csv")
            info_text = f"You opened a {card[2]}-card! {card[4]}, {card[5]}"
            print()
            print(info_text)
            print()
        elif user_input == "2":
            card = generator("community_chest.csv")
            info_text = f"You opened a {card[2]}-card! {card[4]}, {card[5]}"
            print()
            print(info_text)
            print()
        elif user_input == "3":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
