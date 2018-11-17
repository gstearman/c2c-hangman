#
# Code2College HANGMAN Game
#

#
# Definitions (imports, lists, tuples, constants and global variables, etc.)
#
import random  # used for random guessing of words

# List of the body parts
hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]

# Number of guesses allowed is the length of the list of body parts
num_wrong_guesses_allowed = len(hangman_parts)

# List of words to be guessed in the game. Note that these are all in lowercase.
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

#
# Functions
#

########
# draw_hangman
#
def draw_hangman(num_wrong_guesses):
    r"""This function draws the gallows and the body parts for each wrong guess."""

    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)
# draw_hangman


########
# check_if_done
#
def check_if_done(word, guesses):
    r"""This function iterates through the characters in the word.
    If any character in the word has not been guessed, it returns False.
    If every character in the word has been guessed, it returns True.
    """

    for character in word:  # Need to check each chatacter in _____?
        if not character in guesses:
            return False # not done if we find a chaacter that hasn't been guessed.
    return True  # This line is outside the for loop...
# check_if_done


########
# print_guesses
#
def print_guesses(word, guesses):
    r"""This function prints output string with matching letters that were guessed and _s for letters not guessed."""
    output_string = ""
    for char in word:
        if char in guesses:
            output_string = output_string + char + " "   # Need to add the character AND a space to the output_string.
        else:
            output_string = output_string + "_ "   # Need to add the special character for an unguessed letter AND a space.
    print(output_string)
# print_guesses

########
# get_new_guess
#
def get_new_guess(guesses):
    r"""Get a new letter not already guessed. This function returns the lowercase first letter of the input."""
    letter = input("What is your guess? ")
    while (len(letter) != 0) and (letter[0].lower() in guesses):
        letter = input("That letter was already guessed! What is your guess? ")
    return letter[0].lower() # return the single lowercase letter
# get_new_guess


#
# Code execution starts here
#
# Get the player's name and print greeting.
name = input("What is your name? ")
print("Hello, " + name.title() + "! Time to play hangman!")

# Pick a word from the words list using a random index between 0 and length of the list -1
word = words[random.randint(0, len(words) - 1)]

# No wrong guesses at the start.
wrong_guesses = 0
guesses = []
done = False
#
# Main loop which continues until the word is guessed or there are no more body parts left to draw on the hangman
while wrong_guesses < num_wrong_guesses_allowed and not done:
    draw_hangman(wrong_guesses)

    print_guesses(word, guesses)

#    guess = input("What is your guess? ")  # Original code that doesn't check for lowercase, more than one letter or a letter already guessed.
    guess = get_new_guess(guesses)  # Get a new letter not already guessed.

    # If this letter has already been guessed then get another guess that has not been guessed
    while guess in guesses:
        print("You have already guessed that latter, try again!\n", end='')
        guess = input("What is your guess? ")

    # Process the letter which was just guessed.
    if guess in word:
        print("Correct!") # The letter was in the word.
    else:
        print("Wrong!")
        wrong_guesses = wrong_guesses + 1 # The letter was not in the word - add 1 to the count of wrong guesses.

    guesses.append(guess) # Add the wrong letter to the list of guesses.
    print("You've guessed: " + str(guesses)) # Print all the letters which have been guessed so far.

    done = check_if_done(word, guesses) # Has every letter in the word been guessed yet?

# After the while loop is finished and you get here, the game is done.

# Check for a win or a loss now.
if wrong_guesses == num_wrong_guesses_allowed:
    draw_hangman(wrong_guesses) # Draw the hangman with all parts since the final guess was wrong.
    print("Sorry, you lost!\nThe words was: "+word+".")
else:
    print_guesses(word, guesses) # Print the word and list of letters guessed.
    print("You won!") 

# end
