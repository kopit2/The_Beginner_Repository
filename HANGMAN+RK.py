#hangman:by_RK

def translate(word):
    base = ""
    for letter in word:
        if letter in letter_list:
            base = (base + letter)
        else:
            base = base + "_"
    return base
######################################
######################################
won = False
fill = []
guesses = 6
letter_list = [
    "_",
    "-",
    ","
]
word_list = []
subject = input("Enter a subject: ").upper()
word = input("guessing word: ").upper()


######################################
######################################

while not won and guesses > 0:
    print("The subject is: " + subject + "!")
    print(str(guesses) + " Guesses left")
    print(translate(word))
    guess = input("Please enter a word or a letter: ").upper()
    if len(guess) == 1 and guess.isalpha():
        if guess in letter_list:
            print("you have already guessed the letter " + guess)
        elif guess not in word:
            print("The letter " + guess + " is not in the word")
            guesses -= 1
            letter_list.append(guess)
        else:
            print("Good job the letter " + guess + " is in the word\n\n")
            letter_list.append(guess)
            if "_" in translate(word):
                won = False
            else:
                won = True
                print("Good joob " + guess + " is the word\n")
    elif len(guess) == len(word) and guess.isalpha:
        if guess != word:
            if guess in word_list:
                print("You have already guessed the word " + guess)
            elif guess not in word_list:
                print("the word " + guess.upper() + " is not the word\nTry again")
                guesses -= 1
                word_list.append(guess)
        else:
            print("Good joob " + guess + " is the word\nYou won!!!")
            won = True
    else:
        print("Invalid input")
if won:
    print("Winner")
    play_again = input("Do you want to play again?(Y/N): ").upper()
    if play_again == "Y":
        print("Lets play hangman!")
        win = False
        guesses = 6
    else:
        print("Thats a shame")
else:
    print("Out of guesses\n You are the worst hangman player alvie\n")

