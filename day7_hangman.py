#!/usr/bin/env python3

import random

color_red = "\033[91m"
color_green = "\033[92m"
color_yellow = "\033[93m"
color_blue = "\033[94m"
color_magenta = "\033[95m"
color_cyan = "\033[96m"
color_white = "\033[97m"

# drawings
hangman0 = '''
      _______
     |/      
     |      
     |       
     |       
     |      
     |
  ___|___'''
hangman1 = '''
      _______
     |/      |
     |      
     |       
     |       
     |      
     |
  ___|___'''
hangman2 = '''
      _______
     |/      |
     |      (_)
     |       
     |       
     |      
     |
  ___|___'''
hangman3 = '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
  ___|___'''
hangman4 = '''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
  ___|___'''
hangman5 = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
  ___|___'''
hangman6 = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
  ___|___'''
hangman7 = '''      
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
  ___|___'''
hangman_list = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7]

# word lists
words_easy = [
    "apple", "banana", "cherry", "dog", "elephant",
    "flower", "grape", "hat", "ice", "jungle",
    "kite", "lion", "moon", "nest", "orange",
    "pencil", "queen", "rainbow", "sun", "tiger",
    "umbrella", "volcano", "water", "xylophone", "zebra",
    "bird", "car", "duck", "egg", "fish",
    "guitar", "house", "island", "jacket", "kiwi",
    "lemon", "mountain", "noodle", "ocean", "parrot",
    "quilt", "rabbit", "star", "tree", "umbrella",
    "vase", "wolf", "xylophone", "yo-yo", "zeppelin",
    "butterfly", "cat", "dolphin", "elephant", "flamingo",
    "giraffe", "hamburger", "iguana", "jellyfish", "koala",
    "lighthouse", "mango", "night", "octopus", "panda",
    "quokka", "rhinoceros", "snake", "toucan", "unicorn",
    "violin", "waffle", "x-ray", "yacht", "zeppelin",
]
words_medium = [
    "alligator", "balloon", "carousel", "dinosaur", "elephant",
    "firework", "giraffe", "hurricane", "igloo", "jigsaw",
    "kangaroo", "labyrinth", "mysterious", "nebula", "octopus",
    "penguin", "quartz", "rainforest", "seashell", "telescope",
    "umbrella", "volcano", "waterfall", "xylophone", "zeppelin",
    "butterfly", "caterpillar", "dolphin", "elephant", "flamingo",
    "giraffe", "hedgehog", "iguana", "jellyfish", "koala",
    "lighthouse", "macaroni", "narwhal", "octopus", "panda",
    "quokka", "raccoon", "seagull", "toucan", "unicorn",
    "vulture", "wallaby", "x-ray", "yacht", "zeppelin",
    "acorn", "barnacle", "chimpanzee", "dandelion", "earthquake",
    "firefighter", "gorilla", "hummingbird", "iceberg", "jaguar",
    "kettle", "llama", "marmalade", "narwhal", "octopus",
    "pangolin", "quetzal", "rattlesnake", "sloth", "tapir",
    "umbrellabird", "velociraptor", "walrus", "xiphias", "yak",
    "zebrafish", "accordion", "badger", "chameleon", "dolphin",
]
words_hard = [
    "benevolent", "carnival", "delicate", "eclectic", "fantasy",
    "genuine", "haphazard", "incredible", "jubilant", "keen",
    "luminous", "mysterious", "notorious", "optimistic", "paradox",
    "quizzical", "reverence", "symphony", "turbulent", "unique",
    "vibrant", "wanderlust", "xylophone", "yearning", "zeppelin",
    "allegro", "blossom", "clandestine", "dexterity", "eloquent",
    "flourish", "gratitude", "harmony", "imagination", "jovial",
    "kaleidoscope", "labyrinth", "mellifluous", "nonchalant", "orchestra",
    "paradise", "quaint", "resplendent", "serendipity", "tranquil",
    "ubiquitous", "vintage", "whimsical", "xenophile", "yearn",
    "zenith", "altruistic", "bountiful", "charismatic", "dazzling",
    "ecstasy", "fascination", "gleaming", "happiness", "inspiration",
    "juxtaposition", "kudos", "luxurious", "mesmerize", "nurturing",
    "opulent", "panorama", "quixotic", "radiant", "serenity",
    "talisman", "ubiquity", "vivacious", "whisper", "xenodochial",
    "yummy", "zeal", "alluring", "blissful", "captivating",
    "determination", "effervescent", "freedom", "gratitude", "happiness",
    "inspiration", "jubilation", "kindness", "laughter", "motivation",
    "nourishment", "optimism", "passion", "quixotic", "resilience",
    "serenity", "tranquility", "uplifting", "vibrancy", "wonder",
    "xenophile", "youthfulness", "zeal",
]
words = [words_easy, words_medium, words_hard]

is_player_alive = True
player_life = int(7)
hangman_progress = int(0)
is_word_complete = False
used_letters = []
is_letter_correct = False

# Start
print(color_cyan + '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''' + color_white)
print('Welcome to Hangman.\nTry to guess a word letter by letter or, entirely at once.'
      '\nYou die, if you put in 7 wrong letter guesses, or 1 wrong word guess.')
print(hangman0)
difficulty = str(input('\nFirst, choose the difficulty: type "0" for easy, "1" for medium, "2" for hard.\n'))

if difficulty == '0':
    print('Difficulty set to easy.')
elif difficulty == '1':
    print('Difficulty set to medium.')
elif difficulty == '2':
    print('Difficulty set to hard.')
else:
    print('Okay, let\'s try easy first..')
    difficulty = 0
difficulty = int(difficulty)
word = str(words[difficulty][random.randint(0, (len(words[difficulty]) - 1))])
word_list = list(word)
word_len = len(word)
word_progress_str = str('')
word_progress_print = str('')
word_progress_list = []
letter_position = 0

for let in word:
    word_progress_list.append('_ ')
word_progress_str = ''.join(word_progress_list)

# print(word)
print(f'The word has {word_len} letters.\n')
# print(f'DEBUG The word is: {word}')
print(word_progress_str)


def get_guess():
    global word_progress_list
    global word_progress_str
    global word_progress_print
    global player_life
    global hangman_progress
    global used_letters
    global is_letter_correct
    global letter_position
    is_letter_correct = False

    print('''
__________________________________________
//////////////////////////////////////////''')
    guess = str(input('Guess a letter or word: ').lower())
    if len(guess) == 1:
        for letter in word_list:
            # is_letter_correct = False
            # print(f'DEBUG Checking letters')
            # print(f' DEBUG {word_list}')
            # letter_position += 1
            if guess in used_letters:
                # print(f'DEBUG letter: {letter}')
                print(f'Letter "{letter}" already used.')
                is_letter_correct = None
                break
            elif letter == guess:
                word_progress_list[letter_position] = word[letter_position]
                is_letter_correct = True
            # elif letter != guess:
            #     is_letter_correct = False
            letter_position += 1
        if is_letter_correct:
            print(color_green + 'Letter correct.\n' + color_white)
        elif is_letter_correct is False:
            # for letter in word:
            #     letter_position += 1
            player_life -= 1
            hangman_progress = 7 - player_life
            # print(f'player life is {player_life}')
            # print(f'hangman progress is {hangman_progress}')
            print_hangman()
            is_letter_correct = None
        used_letters.append(guess)
        letter_position = 0
        # print(f'DEBUG used letters: {used_letters}')
    elif len(guess) == len(word):
        if guess == word:
            word_complete()
        else:
            out_of_guesses()
    else:
        print(f'Please put in either one letter, or a word with {word_len} letters.')
        get_guess()

    word_progress_str = ''.join(word_progress_list).lower()
    word_progress_print = ' '.join(word_progress_list).upper()
    print(word_progress_print)
    if word_progress_str == word:
        word_complete()


def word_complete():
    print(color_green + f'You win! You had {player_life} guesses left.' + color_white)
    exit()


def out_of_guesses():
    print(color_red + f'You\'re dead! The correct word is "{color_green + word}".' + color_white)
    exit()


def print_hangman():
    print(color_red + 'Wrong letter.' + color_white)
    print(hangman_list[hangman_progress])


while is_player_alive:
    if player_life > 0 and not is_word_complete:
        get_guess()
    elif player_life <= 0:
        out_of_guesses()
    elif is_word_complete:
        word_complete()
