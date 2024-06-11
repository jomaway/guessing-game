# guessing-game v1.0 - 2024-05-17 - Erste spielbare version mit highscore
# guessing-game v2.0 - 2024-06-04 - Exceptions mit try ... except abfangen
# guessing-game v3.0 - 2024-06-07 - Funktion play und play again Möglichkeit.

import random

def play():
    number = random.randint(1, 100)
    user_wins = False
    score = 0

    while not user_wins:  # alternative: user_wins == False
        score += 1 # kurzform für: score = score +1

        try:
            guess = int(input("Geben Sie eine Zahl zwischen 1 und 100 ein:"))
            if guess < 1 or guess > 100:
                raise ValueError
        except ValueError:
            print("Falsche eingabe!")
            continue

        if number == guess:
            print(f"Yes, {number} is the winner. Score: {score}")
            user_wins = True
        elif guess > number:
            print("Die gesuchte Zahl ist kleiner.")
        else:
            print("Die gesuchte Zahl ist größer.")
    # bis hier ist die function play

def save_score(score):
    # speichert den HIGHSCORE in einer DATEI ab.
    #TODO: implementieren Sie diese Funktion.
    pass

while True:  # Dauerschleife
    play()

    correctUserInput = False
    while not correctUserInput:
        prompt = input("Wollen Sie noch eine Runde spielen? [y/n]")

        if prompt == 'n':
            exit()
        elif prompt == 'y':
            correctUserInput = True
        else:
            print("Falsche eingabe nur y oder n erlaubt.")