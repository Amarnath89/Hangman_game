import random
from   hangman_list import hangman


words = ['amarnath','gokul','bharani','gowtham','ezhil']
word = random.choice(words)


def start_game(word):
    guess_word = ["_" for i in word ]
    tries = 0
    print(hangman[tries])

    #list of word convert to string
    print("guess word :{}".format(" ".join(guess_word)))
    
    while True:
        user_input = input("Enter your guess [a to z]:")
        if not user_input.isalpha():
            print("Enter valid inputs only [a to z]:")
            continue
        if user_input in word:
            indexes = [i for i in range(len(word)) if word[i]== user_input]
            for index in indexes:
                guess_word[index] = user_input
            print("*"*75)
            print("your guess is correct :{}".format("".join(guess_word)))
        
        elif "".join(guess_word) == word:
            return "Wow! You Guessed " 
       
        else:
            tries = tries + 1
            print(hangman[tries])
            if tries == 6:
                return "Sorry! Game Over."
            print("Sorry! Try Again : {}".format("".join(guess_word)))



if __name__ == '__main__':
    while True:
        start_game(word)
        play_agin = input("Do you want play agin y/n :")
        if play_agin =='y':
            word = random.choice(words)
            continue
        else:
            break    




