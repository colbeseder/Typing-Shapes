'''
Inspired by Matt Parker's video https://youtu.be/Mf2H9WZSIyw?t=843

Find the most common word shape on a Qwerty keyboard

Run command:
    $ python mostCommonShape.py WORD_LIST_FILE [OUTPUT_FILE]

If an output file is provided, the full set of non-trivial shapes will be written there, including the number of occurences of each.

result (for Qwerty):
    The most common shape had 4 occurences:
    ['dede', 'juju', 'kiki', 'lolo']

result (for Dvorak):
    The most common shape had 6 occurences:
    ['dada', 'hoho', 'lyly', 'nunu', 'sisi', 'tete']

'''

import sys

#Qwerty
ROWS = ["QWERTYUIOP","ASDFGHJKL","ZXCVBNM"]

#Dvorak
# ROWS = ["   PYFGCRL", "AOEUIDHTNS", " QJKXBMWVZ"]

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
        if value is None or value < 3 or len(key) < 34 : # ~word length less than 4
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

def write_count_to_file(filename, counts):
    with open(filename, 'w') as f:
        for key, value in counts.items():
            if value is None:
                continue
            f.write("%s: %s\n" %(value, key))

if __name__ == "__main__":
    # parse args
    words_file = sys.argv[1]
    out_file = None
    if len(sys.argv) > 2:
        out_file = sys.argv[2]

    with open(words_file) as file:
        lines = file.readlines()
    words = [line.rstrip() for line in lines]
    paths = map(get_path, words)
    counts = get_duplicate_count(paths)

    if out_file is not None:
        write_count_to_file(out_file, counts)

    highest = max(counts, key=counts.get)
    matches = find_matches(parse_path(highest), words)
    print("The most common shape had %s occurences:"%(len(matches)))
    print(matches)
