import random
'''
Hangman.py, created by Andrew Lyle
'''
#create list of random words
#TODO: add file with more random words
words = ['heuristic','algorithm','template','pseudo-code','artificial','flow-chart','ethics','media','privacy','teamwork','pairs',
         'perseverance','resilience','google','resource','sequence','repetition','function','selection','procedure','communication',
         'integer','floating','boolean','field','syntax','binary','ternary','octal','decimal','hexadecimal','debug','source',
         'equation','rhythm','matching','symmetry','cipher','byte','kilobyte','megabyte','gigabyte','terabyte','petabyte','deductive',
         'inductive','logistics','algorithmic','decomposition','abstraction','generalisation','evaluation','creativity','computational',
         'education','pedagogy','enquiry','discovery','intuitive','machine','hardware','central','digital','analog','analogue','top-down',
         'variable','constant','mutable','network','online','offline','editor','iterate','pixels','software','python','assembler',
         'argument','graphics','callback','array','database','run-time','interpreter','compiler','bandwidth','youtube']
guesses = []
solved = True
totalGuesses = 0
maxGuesses = 6 #maximum number of player guesses.
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def get_random_word():
    return random.choice(words)

def display_puzzle(playWord):
    global solved
    str = ""
    for i in playWord:
        if i in guesses:
            str += i+" "
        else:
            str += "_ "
            solved = False
    return str

def add_guess_letter(letter, playWord):
    global totalGuesses
    if len(letter) > 1:
        print("Incorrect input. Please choose a letter")
    elif letter.isalpha() == False:
        print("Incorrect input. Please choose a letter")
    elif letter not in guesses:
        guesses.append(letter)
        if letter not in playWord.upper():
            totalGuesses += 1
    else:
        print("Please try another letter.")
    
print("Welcome to hangman!.. Hope you enjoy this game!")
playWord = get_random_word()

while True:
    solved = True
    curWordDisplay = display_puzzle(playWord.upper())
    print("------------------------\n\n"+curWordDisplay+"\n\nUsed Letters: ")
    print(guesses)    

    print(HANGMANPICS[totalGuesses])
    if solved == True:
        print("Congratulations! You solved the puzzle!")
        break
    elif totalGuesses >= maxGuesses:
        print("Game over :(\n\nThe word was: "+playWord)
        break
    else:
        guessInput = input("Enter a Letter: ").upper()
        add_guess_letter(guessInput, playWord)
    


