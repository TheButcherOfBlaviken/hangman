from random import choice
import json
import re


# class Hangman

#     def __init__(self):
#         """
#         Initializing a Hangman game
#         """        
#         self.matched_letters, self.guesses = [], []
matched_letters, guesses = [], []

def destroy():
    """
    Destroys any values stored in matched_letters and guesses made.
    """
    global matched_letters, guesses
    matched_letters, guesses = [], []
    

def generate_word():
    """
    Generates a random word from a given list.

    Returns:
        dict: `Word`: The word itself. `Type`: What type of of thing it is. `Desc`: More detailed description.
    """
    with open('words.json', 'r', encoding='utf-8') as f:
        content = f.read()
        words = json.loads(content)

    # word_data = choice(words['words'])
    word_data =         {
            "Word": "Bat man",
            "Type": "Fictional character",
            "Desc": "Character from DC universe"
        }

    return word_data


def word_analyzer(word_data):
    """Analyzes the generated word.

    Args:
        word_data (dict): Contains the generated word and further details about the word.

    Returns:
        tuple: metadata of the generated word.
    """
    word = word_data['Word']
    word_length = len(word)
    word_type = word_data['Type']
    word_desc = word_data['Desc']

    word_metadata = (word, word_length, word_type, word_desc)

    return word_metadata


def print_hint(word_length, word_type, word_desc, matches=False):
    """
    
    """
    print(f"""        ==============================\n
        #### Hint ####
        Letters: {word_length}
        Type: {word_type}
        Description: {word_desc}
        ==============================""")

    print("\n" + " ".join(matched_letters))


def hint_builder(word, word_length):
    """Builds the hint for the user.

    Args:
        word (str): The generated word.
        word_length (int): Length of the generated word.

    Raises:
        ValueError: If an abnormal character is entered, an error is raised.
    """
    alphanumerals = re.compile(r'[a-zA-Z0-9]')
    for letter in range(word_length):
        if re.search(alphanumerals, word[letter]):
            matched_letters.append("_ ")
        elif re.search('\s', word[letter]):
            matched_letters.append(" ")
        else:
            print("Abnormal word selection")
            raise ValueError


def show_hint(word, word_length, word_type, word_desc):
    """
    Shows initial hint to the user and the progress of the guessing after each turn.

    Arguments:
        word (dict): dict of the generated word.
        letters (list): the guessed letters of the word at any given point in time. Initially, an empty list.

    Returns:
        list: a list of all the guessed letters.

    """
    if matched_letters:
        print_hint(word_length, word_type, word_desc, matches=True)
    else:
        hint_builder(word, word_length)
        print_hint(word_length, word_type, word_desc)


def update_letters(matches):
    """Updates the hidden hint with the matched letters.

    Args:
        matches (list(dict)): A list contanining matched letters and their indexes as individual dictionaries.

    Returns:
        bool: Returns `False` if there are no matches in the word for the letter(s) guess by the user. Returns `True` otherwise.
    """
    if matches:
        for match in matches:
            for value in match['Indexes']:
                matched_letters[value] = match['Guess']
    else:
        return bool(False)

    return bool(True)


def guess_matcher(guess, word):
    """Checks whether the guessed letter or letters matches the any of the letter(s) in the chosen word.

    Args:
        guess (str): The guess made by the user.
        word (str): The target word chosen at random by the game.

    Returns:
        list(dict) | None: If some matches are found, the list of matched letters and the index of the word in which they appear are returned.
                                Otherwise, None is returned to show that nothing matched. 
    """
    pattern = re.compile(fr'{guess}', re.IGNORECASE)
    matches = pattern.finditer(word)

    matched = []
    # if len(guess) == 1:
    indexes = [match.start() for match in matches if match]
    if indexes:
        match_and_indexes = {'Guess': guess, 'Indexes': indexes}
        matched.append(match_and_indexes)
        return matched
    else:
        return None

    # What if someone guesses the whole thing?
    # elif len(guess) > 1:
    #     if pattern.fullmatch(word):
    #         return 'Fullmatch'
    #     else:
    #         return is_alive == False


def input_validator(guess, word):
    """Checks whether the user input is valid or not. If it is an invalid entry, the function returns `False`.
        If the entry is valid, the entry is searched and matching indexes are returned.

    Args:
        guess (str): The letter or letters that a player guessed.
        word (dict): The target word str and its type, and description in a dict format.

    Returns:
        bool: Returns `False` if the guess/entry is an invalid character. Otherwise calls `guess_matcher` function to match the guess with the word.
    """
    invalid_inputs = re.compile(r'[^a-zA-Z0-9]')

    if invalid_inputs.match(guess) != None:
        print("Please enter an alphanumeric character. Symbols are not allowed.")
        return bool(False)

    else:
        return guess_matcher(guess, word)


def hangman():
    """
    Main function of the game.
    """

    word_data = generate_word()
    word, word_length, word_type, word_desc = word_analyzer(word_data)
    show_hint(word, word_length, word_type, word_desc)
    
    game_is_active = True
    while game_is_active:
        tries_left = 10
        while tries_left >= 0:
            if str("".join(matched_letters)).lower() != word.lower(): 
                print(f"\nTries left: {tries_left}")
                guess = input("Take a guess: ")
                # print("Type 'help', if you need to see the hint again.")
                # if guess.lower() == 'help':
                #     print_hint(word)
                # else:
                is_input_valid = input_validator(guess, word)
                if is_input_valid == False:
                    continue
                else:
                    matches = is_input_valid
                    is_matched = update_letters(matches)
                    if is_matched:
                        show_hint(word, word_length, word_type, word_desc)
                    else:
                        tries_left -= 1
                    if tries_left < 0:
                        print("Man hanged!")
                    else:
                        print(f"Tries left: {tries_left}\n")
            else:
                return print("Congratulations! You guessed it right!")
        else:
            print("\nSorry you are out of tries!")
            print(f"The correct answer was {word}!")
            replay = input("Play again? (Y/n): ").lower()
            if replay == 'y':
                destroy()
                hangman()
            elif replay == 'n':
                return print("\nThank you for playing!\n")
            else:
                return print("\nI'm going to assume that you will not play again.\n")
            

hangman()
