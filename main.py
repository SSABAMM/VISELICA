import random
from enum import Enum

#choice_in_menu = ''
s = list(map(str.strip,open('dictionary.txt',encoding='utf-8').readlines()))

class Commands(Enum):
    START = 1
    END = 2

def get_random_word_from_dict(x):
    word = random.choice(s)
    return word

def get_encrypted_word(x):
    return '*'*len(x)

def find_letter_in_word(char, word, current):
    formed_string = ''
    is_find = False
    for i, letter in enumerate(word):
        if letter == char or letter.lower() == char:
            formed_string += letter
            is_find = True
        else:
            formed_string+=current[i]
    if is_find:
        return formed_string
    else:
        return current

def print_hangman(lives, word):
    if lives == 1:
        print(
              '|+---+\n'
              '|\n'
              '|\n'
              '|\n'
              '|\n'
              '=========\n'
              'You have 3 lives!')
    elif lives == 2:
        print(
            '|+---+\n'
            '|    |\n'
            '|    O\n'
            '|\n'
            '|\n'
            '=========\n'
            'You have 2 lives!')
    elif lives == 3:
        print(
            '|+---+\n'
            '|    |\n'
            '|    O\n'
            '|   /|\ \n'
            '|\n'
            '=========\n'
            'You have 1 lives!\n')
    elif lives == 4:
        print(
            '|+---+\n'
            '|    |\n'
            '|    O\n'
            '|   /|\ \n'
            '|   / \ \n'
            '=========\n'
            f'You DIED! YOUR WORD: {word}\n')

def congrat_winner_game(word):
    print(f'You WIN! It was word "{word}"!\n')


def print_separator_line():
    print('_________________________________________\n')
def print_found_letters(found_letters):
    print(f'Founded letters: {" ".join(found_letters).upper()}')
    print_separator_line()
def validation_entered_letter(input_letter):
    return (input_letter.isalpha() or input_letter.islower() or 'а' <= input_letter <= 'я' or input_letter == 'ё') and len(input_letter)==1

def validation_of_choice_in_menu(choice_in_menu):
    return choice_in_menu != 'n' and choice_in_menu != 'e'
def start_game_menu(choice_in_menu):
    while choice_in_menu != 'e':
        print('RULES:\n'
              'N - new game\n'
              'E - exit\n\n')
        while validation_of_choice_in_menu(choice_in_menu):
            print('Input your choice:')
            choice_in_menu=input().lower()
            #if choice_in_menu == Commands.START.value:


            if validation_of_choice_in_menu(choice_in_menu):
                print('You print the wrong letter! Try again.')
        if choice_in_menu == 'n':
            start_main_game(choice_in_menu)
        elif choice_in_menu == 'e':
            print('Goodbye!!')
            exit(1)

def start_main_game(choice_in_menu):
    if choice_in_menu == 'n':
        found_letters = []
        input_letters_list = []
        count_lives = 0
        print_separator_line()
        #word = get_random_word_from_dict(choice_in_menu)
        word = 'ёжик'
        mask_word = get_encrypted_word(word)
        print(f'Your word: {mask_word} {word} \n')
        while '*' in mask_word:
            print('Print the letter:')
            input_letter = input().lower()
            if not validation_entered_letter(input_letter) :
                print('Invalid input. Please input cyrillic lowercase letter!')
                continue
            new_mask_word = find_letter_in_word(input_letter, word, mask_word).lower()
            if new_mask_word != mask_word:
                mask_word = new_mask_word.lower()
                found_letters.append(input_letter)
                print(new_mask_word)
                if new_mask_word == word: congrat_winner_game(word)
                print_separator_line()
                input_letters_list.append(input_letter)




            else:
                if input_letter in input_letters_list:
                    print('You entered this letter earlier!')
                    continue
                input_letters_list.append(input_letter)
                count_lives += 1
                print_hangman(count_lives,word)
                if count_lives == 4:
                    if found_letters:
                        print_found_letters(found_letters)
                    print_separator_line()
                    found_letters.clear()
                    input_letters_list.clear()
                    break
                print('Hidden word:',new_mask_word)
                print_separator_line()
        start_game_menu(1)

if __name__ == '__main__':
    start_game_menu(1)

