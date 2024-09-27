import random

#● ┌ ─ ┐ │ └ ┘


#"┌─────────┐"
#"│         │"
#"│         │"
#"│         │"
#"└─────────┘"
def main():
    
        dice_art = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│ ●       │",
                "│         │",
                "│       ● │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│ ●       │",
                "│    ●    │",
                "│       ● │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│ ●     ● │",
                "│         │",
                "│ ●     ● │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│ ●     ● │",
                "│    ●    │",
                "│ ●     ● │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘")
        }

        dice = []
        total = 0
        
        def num_of_dice(msg = "How many dice to roll?: "):
            try:
                inp = int(input(msg))
            except ValueError:
                print("Invalid character, please type a number 1 through 6: ")
                inp = num_of_dice(msg)
            return inp
        
        numdice = num_of_dice("How many dice to roll?: ")   
        
        for die in range(numdice):
            dice.append(random.randint(1, 6))

        #for die in range(num_of_dice):
        #    for line in dice_art.get(dice[die]):
        #        print(line)

        for line in range(5):
            for die in dice:
                print(dice_art.get(die)[line], end="")
            print()

        for die in dice:
            total += die
        print(f"Your total is: {total}")

        Repeat = input("Roll again? (y/n) ")
        if Repeat == "y":
            main()
        else:
            exit()
              
main()