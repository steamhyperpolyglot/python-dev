import sys
from string import punctuation
import json
from nltk.corpus import cmudict

# load dictionary of words in haiku corpus but not in cmudict
with open('missing_words.json') as f:
    missing_words = json.load(f)

cmudict = cmudict.dict()

def count_syllables(words):
    """
    Use corpora to count syllables in English word or phrase.
    """

    # prep words for cmudict corpus
    words = words.replace('-', ' ')
    words = words.lower().split()
    num_syll = 0
    for word in words:
        word = word.strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word in missing_words:
            num_syll += missing_words[word]
        else:
            for phonemes in cmudict[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        num_syll += 1
    return num_syll

def main():
    while True:
        print("Syllable Counter")
        word = input("Enter word or phrase; else press ENTER to Exit: ")
        if word == '':
            sys.exit()
        try:
            num_syllables = count_syllables(word)
            print("number of syllables is {} is: {}".format(word, num_syllables))
            print()
        except KeyError:
            print("Word not found. Try again.\n", file=sys.stderr)
    
if __name__ == '__main__':
    main()
