from random import choice
import json
import re


class Hangman:
    """The entire game is contained within this class.
    """    

    def __init__(self):
        """
        Initializing a Hangman game
        """        
        pass
        

    def generate_word(self):
        """
        Generates a random word from a given list.

        Returns:
            dict: A dictionary conatining the following:
            
                word (str): The word itself. 
                
                type (str): What type of of thing it is. 
                
                desc (str): More detailed description.
        """
        with open('words.json', 'r', encoding='utf-8') as f:
            content = f.read()
            words = json.loads(content)

        word_data = choice(words['words'])
        #* Test data
        # word_data =         {
        #         "Word": "Bat man",
        #         "Type": "Fictional character",
        #         "Desc": "Character from DC universe"
        #     }

        return word_data


    @staticmethod
    def _word_analyzer(word_data):
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


    def print_hint(self, word_length, word_type, word_desc):
        """Prints the hint for the user.

        Args:
            word_length (int): Number of alphabets in the target word.
            word_type (str): Type of the target word e.g. book, movie, song, fictional character etc.
            word_desc (str): Detailed description of the target word.
        """                        
        print(f"""        
                         \n======================================================================================================================
            #### Hint ####
            Letters: {word_length}
            Type: {word_type}
            Description: {word_desc}
======================================================================================================================\n""")

        print("\n" + " ".join(self.matched_letters).upper())

    @staticmethod
    def _hint_builder(self, word, word_length):
        """Builds the hint for the user.

        Args:
            word (str): The generated word.
            word_length (int): Length of the generated word.
        """
        alphanumerals = re.compile(r'[a-zA-Z0-9]')
        for letter in range(word_length):
            if re.search(alphanumerals, word[letter]):
                self.matched_letters.append("_ ")
            elif re.search('\s', word[letter]):
                self.matched_letters.append(" ")
            else:
                print("Abnormal word selection")


    def show_hint(self, word, word_length, word_type, word_desc):
        """
        Shows initial hint to the user and the progress of the guessing after each turn.

        Args:
            word (dict): dict of the generated word.
            letters (list): the guessed letters of the word at any given point in time. Initially, an empty list.
        """
        if not self.matched_letters:
            self._hint_builder(word, word_length)    
        self.print_hint(word_length, word_type, word_desc)


    @staticmethod
    def _update_letters(self, matches):
        """Updates the hidden hint with the matched letters.

        Args:
            matches (list(dict)): A list contanining matched letters and their corresponding start and end indexes.

        Returns:
            bool: `False` if there are no matches in the word for the letter(s) guess by the user. `True` otherwise.
        """
        if matches:
            for match in matches:
                for x, y in match['Indexes']:
                    self.matched_letters[x:y] = match['Guess']
            return bool(True)
        
        else:
            return bool(False)


    @staticmethod
    def _guess_matcher(self, guess, word):
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
        indexes = [(match.start(), match.end()) for match in matches if match]
        if indexes:
            match_and_indexes = {'Guess': guess, 'Indexes': indexes}
            matched.append(match_and_indexes)
            return matched
        else:
            return None


    @staticmethod
    def _input_validator(self, guess, word):
        """Checks whether the user input is valid or not. If it is an invalid entry, the function returns `False`.
            If the entry is valid, the entry is searched and matching indexes are returned.
            Examples of invalid entries are:
                1. Symbols
                2. Special characters
                3. Spaces 

        Args:
            guess (str): The letter or letters that a player guessed.
            word (dict): The target word str and its type, and description in a dict format.

        Returns:
            bool: `False` if the guess/entry is an invalid character. Otherwise calls `guess_matcher` function to match the guess with the word. 
            Invalid characters are symbols and spaces.
        """
        invalid_inputs = re.compile(r'[^a-zA-Z0-9]')

        if invalid_inputs.match(guess) != None or guess == " ":
            return bool(False)
        else:
            return self._guess_matcher(guess, word)


    def hangman(self):
        """The main function of the game.

        Returns:
            str
        """              
        self.word_data = self.generate_word()
        self.word, self.word_length, self.word_type, self.word_desc = self._word_analyzer(self.word_data)
        
        self.matched_letters, self.guesses = [], []
        self.show_hint(self.word, self.word_length, self.word_type, self.word_desc)
        
        game_is_active = True
        while game_is_active:
            tries_left = 10
            while tries_left >= 0:
                if str("".join(self.matched_letters)).lower() != self.word.lower(): 
                    print(f"\nTries left: {tries_left}")
                    guess = input("Take a guess: ")
                    is_input_valid = self._input_validator(guess, self.word)
                    if is_input_valid == False:
                        print("""\n====================\nPlease enter an alphanumeric character. Symbols and spaces are not allowed.\n====================\n""")
                        continue
                    else:
                        matches = is_input_valid
                        is_matched = self._update_letters(matches)
                        if is_matched == False:
                            tries_left -= 1
                        self.show_hint(self.word, self.word_length, self.word_type, self.word_desc)
                        if tries_left < 0:
                            print("Man hanged!")
                else:
                    print("Congratulations! You guessed it right!\n")
                    play_again = input("Wanna play again? (Y/n): ")
                    if play_again.lower() == 'y':
                        self.hangman()
                    else:
                        return print("\nThank you for playing!")
            else:
                print("\nSorry you are out of tries!")
                print(f"The correct answer was {self.word}!")
                replay = input("Play again? (Y/n): ").lower()
                if replay == 'y':
                    self.hangman()
                else:
                    return print("\nThank you for playing!\n")
                break

                
if __name__ == '__main__':
    hangman_game = Hangman()
    hangman_game.hangman()
