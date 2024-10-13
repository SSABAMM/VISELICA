import random

k=''
s = []

with open("slovar'.txt", encoding='utf-8') as f:
    for i in f:
        s.append(i.strip())

def rand_word(x):
    word = random.choice(s)
    return word

def star_word(x):
    return '*'*len(x)

def find_letter(x,word,current):
    slovo = ''
    flag = False
    for i, letter in enumerate(word):
        if letter == x or letter.upper() == x:
            slovo += letter
            flag = True
        else:
            slovo+=current[i]
    if flag:
        return slovo
    else:
        return current

def print_hangman(times):
    if times == 1:
        print(
              '___________.._______\n'
              '| .__________))______|\n'
              '| | / /      ||\n'
              '| |/ /       ||\n\n'
              'You have 2 lives!')
    elif times == 2:
        print(
            '___________.._______\n'
            '| .__________))______|\n'
            '| | / /      ||\n'
            '| |/ /       ||\n'
            '| | /        ||.-''.\n'
            '| |/         |/  _  \ \n'
            '| |          ||  `/,| \n'
            "| |          (\\`_.' \n"
            "| |         .-`--'. \n"
            "| |        /Y . . Y\ \n"
            "| |       // |   | \\ \n"
            "| |      //  | . |  \\ \n"
            "| |     ')   |   |   (` \n\n"
            'You have 1 lives!')
    elif times == 3:
        print(
            '___________.._______\n'
            '| .__________))______|\n'
            '| | / /      ||\n'
            '| |/ /       ||\n'
            '| | /        ||.-''.\n'
            '| |/         |/  _  \ \n'
            '| |          ||  `/,| \n'
            "| |          (\\`_.' \n"
            "| |         .-`--'. \n"
            "| |        /Y . . Y\ \n"
            "| |       // |   | \\ \n"
            "| |      //  | . |  \\ \n"
            "| |     ')   |   |   (` \n"
            "| |          ||'|| \n"
            "| |          || || \n"
            "| |          || || \n"
            "| |          || || \n"
            'You DIED!\n'
            '___________________________________\n')

def start_game(k):
    print('RULES:\n'
          'N - new game\n'
          'E - exit\n\n')
    while k != 'N' and k != 'E':
        print('Input your choice:')
        k=input()
        if 'N' not in k and 'E' not in k:
            print('You print the wrong letter! Try again.')
    start_main_game(k)

def start_main_game(k):
    if k == 'N':
        times = 0
        print('\n\n_________________________________________\n')
        word = rand_word(k)
        mask_word = star_word(word)
        print(f'Your word: {mask_word} \n')
        while '*' in mask_word:
            print('Print the letter:')
            firstl = input()
            if not firstl.isalpha() or not firstl.islower() or not 'а' <= firstl <= 'я':
                print('Invalid input. Please input cyrillic lowercase letter!')
                continue
            new_mask_word = find_letter(firstl, word, mask_word).upper()
            if new_mask_word != mask_word:
                mask_word = new_mask_word.upper()
                print(new_mask_word ,'\n\n_________________________________________\n')
            else:
                times += 1
                print_hangman(times)
                if times == 3:
                    start_game(1)
    elif k == 'E':
        print('Goodbye!!')
        exit(1)


start_game(k)

