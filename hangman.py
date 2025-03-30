

# Hangman game

import random

words = ("Cybersecurity", "Forensics", "Scripting", "Firewall", "Encryption", 
         "Python", "Terminal", "Anonymousi", "Phishing", "Exploit")

hangman_art = {
        0: ( 
        " ",
        " ",
        " ",
        ),

    1: ( " 0 ",
        " ",
        " ",
        ),

    2: ( " 0 ",
        " |",
        " ",
        ),

    3: ( " 0 ",
        " /|",
         "  ",
            ),

    4: ( " 0 ",
        " /|\\",
        " ",
        ),

    5: ( " 0 ",
        " /|\\",
        "  /",
        ),

    6: ( " 0 ",
        " /|\\",
        "  /\\",
        ),
}





def display_man(wrong_message):
    print("**************")
    for line in hangman_art[wrong_message]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main ():
    answer = random.choice(words).lower()
    
    
    given_hint = ["_"]* len(answer)  # it prints _ as a length of selected words

    # print(given_hint)
    wrong_guess = 0
    guessed_letter = set()    # guessed_letter is an empty set, ready to store unique values. If you add a letter multiple times, it will only be stored once.
    
    is_running = True

    while is_running :
        display_man(wrong_guess)
        display_hint(given_hint)
        # display_answer(answer)
        guess = input("Enter  a letter :").lower()


             # input validation

        if len(guess)!=1 or not  guess.isalpha() :
             print("Enter single letter only : ")
             continue
         
        

        if guess in guessed_letter :
            print(f"{guess} is already there")
            continue

        guessed_letter.add(guess)

        if guess in answer:
           
           for i in range(len(answer)):
               if answer[i]== guess:
                   given_hint[i]=guess
               
        else:
            wrong_guess+= 1
            print(f"Wrong guess! Attempts left: {6 - wrong_guess}")

        if "_" not in given_hint:
            print("Congratulations! You guessed the word:", answer)
            break

        # Check if the player has lost
        if wrong_guess >= 6:
            display_man(6)
            print("Game Over! The correct word was:", answer)
            break

if __name__ == "__main__" :
    main()