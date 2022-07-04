'''
Inspired by Matt Parker's video https://youtu.be/Mf2H9WZSIyw?t=843

Find the most common word shape on a Qwerty keyboard

Run command:
    $ python mostCommonShape.py WORD_LIST_FILE [OUTPUT_FILE]

If an output file is provided, the full set of non-trivial shapes will be written there, including the number of occurences of each.

WORD_LIST_FILE should be a text file with a separate word on each line.

result (for Qwerty):
    The most common shape of at least 4 letters had 4 occurences:
    ['dede', 'juju', 'kiki', 'lolo']
    ['eyey', 'yoyo', 'ruru', 'titi']

result (for Dvorak):
    The most common shape of at least 4 letters had 6 occurences:
    ['dada', 'hoho', 'lyly', 'nunu', 'sisi', 'tete']

'''

import sys

KEYBOARD = "qwerty"
MINIMUM_WORD_LENGTH = 6

keyboards = {
    "qwerty": ["QWERTYUIOP","ASDFGHJKL","ZXCVBNM"],
    "dvorak": ["   PYFGCRL", "AOEUIDHTNS", " QJKXBMWVZ"]
}

ROWS = keyboards[KEYBOARD]

# Returns x, y (place in row, row number)
def get_letter_location(c):
    c = c.upper()
    for y, row in enumerate(ROWS):
        if c in row:
            for x, letter in enumerate(row):
                if c == letter:
                    return x, y
    return None

# Difference in (x,y) from previous key)
def get_path(word):
    if len(word) < MINIMUM_WORD_LENGTH:
        return None
    locations = list(map(get_letter_location, word))
    if None in locations:
        return None
    path = [(0,0)]
    for i in range(1, len(locations)):
        n = (locations[i][0] - locations[i-1][0], locations[i][1] - locations[i-1][1])
        path.append(n)
    return path

# Find all words in list with the target path
def find_matches(target, words):
    matches = []
    for word in words:
        if get_path(word) == target:
            matches.append(word.lower())
    return matches

# How many occurences of each path were there -> returns dict of {path: count}
def get_duplicate_count(arr):
    counts = {}
    for raw_item in arr:
        if raw_item is None:
            continue
        item = str(raw_item)
        if item in counts:
            counts[item] +=1
        else:
            counts[item] = 1
    filter_out_trivials(counts)
    return counts

def filter_out_trivials(counts):
    to_pop = []
    for key, value in counts.items():
        if value is None or value < 2:
            to_pop.append(key)
    for key in to_pop:
        counts.pop(key)

# Unhash paths from string
def parse_path(s):
    parts = s.strip('[]').split(',')
    path = []
    i = 0
    while i < len(parts):
        pair = ( int(parts[i].strip("() ")), int(parts[i+1].strip("() ")) )
        path.append( pair )
        i += 2
    return path

def find_duplicate_paths(words, keyboard):
    paths = map(get_path, words)
    counts = get_duplicate_count(paths)
    return counts

def print_detailed_results(words, keyboard, min_length):
    counts = find_duplicate_paths(words, keyboard)
    
    highest = max(counts, key=counts.get)
    
    print("The most common shape of at least %s letters on a %s keyboard has %s occurences:"%(MINIMUM_WORD_LENGTH, KEYBOARD, counts[highest]))
    for key, value in counts.items():
        if value == counts[highest]:
            matches = find_matches(parse_path(key), words)
            print("%s (%s letters)" %(matches, len(matches[0])))

def get_words(words_file):
    with open(words_file) as file:
        lines = file.readlines()
    return set([line.rstrip().lower() for line in lines])


def write_count_to_file(filename, counts):
    with open(filename, 'w') as f:
        for key, value in counts.items():
            if value is None:
                continue
            f.write("%s: %s\n" %(value, key))

if __name__ == "__main__":
    # parse args
    words_file = sys.argv[1]

    if len(sys.argv) > 2:
        MINIMUM_WORD_LENGTH = int(sys.argv[3])
    if len(sys.argv) > 3:
        KEYBOARD = sys.argv[4]

    words = get_words(words_file)
    print_detailed_results(words, KEYBOARD, MINIMUM_WORD_LENGTH)