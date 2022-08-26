from win32com.client import Dispatch
import random

from termcolor import cprint


class game:

    def __init__(self):
        self.chances = 0
        self.opp_win = 0
        self.user_win = 0
        self.user = ''
        self.opp = ''

    def draw(self, user, opp):
        print("Oops!!\nMatch draw")
        print("You chooses", user, "And your opponent chooses", opp)
        self.chances += 1

    def win(self, user, opp):
        print(f"Hurray\nYou win!")
        print(f"You chooses {user} And your opponent chooses {opp}")
        self.user_win += 1
        self.chances += 1

    def lose(self, user, opp):
        print(f"You Loose!!\t\tDont worry, try again.")
        print(f"You chooses {user} And your opponent chooses {opp}")
        self.chances += 1
        self.opp_win += 1

    def finalScore(self):
        print(f"Your final score is:- {self.user_win}\nYour opponent score :-  {self.opp_win}")
        print("Hope you enjoyed!\nCome soon!!")

    def run(self):
        while self.chances != 10:

            adi = ['s', 'w', 'g']
            self.opp = random.choice(adi)

            self.user = input("Enter 's' for Snake, 'w' for Water and 'g' for Gun.\n")

            if self.user == self.opp:
                self.draw(self.user, self.opp)

            if (self.user == 's' and self.opp == 'w') or (self.user == 'g' and self.opp == 's') or (self.user == 'w' and self.opp == 'g'):
                self.win(self.user, self.opp)

            elif (self.user == 'w' and self.opp == 's') or (self.user == 'g' and self.opp == 'w') or (self.user == 's' and self.opp == 'g'):
                self.lose(self.user, self.opp)

        self.finalScore()
        self.again_play()

    def again_play(self):
        play_again = input(
            "\t\t\tWant to play again?\nEnter 'y' for Yes and 'N' for No.\n")
        if play_again == 'y':
            game()
        elif play_again == 'N':
            print("\t\t*Thank You*!!\nCome Back Soon!")
        else:
            print("Wrong input.Please type 'y' or 'n' only.")
            self.again_play()


if __name__ == "__main__":
    cprint("#" * 50, "magenta")
    cprint(f"SNAKE WATER GUN GAME ".center(50), "yellow")
    cprint("#" * 50, "magenta")
    print("WELCOME!")
    gm = game()
    gm.run()
