#!/usr/bin/env python

# Packages and nltk requirements
import nltk
import argparse
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from collections import Counter

# Counter Function
def count_verbs_nouns(text):
    tokens = nltk.word_tokenize(text.lower())
    text = nltk.Text(tokens)
    tags = nltk.pos_tag(text)

    counts = Counter(tag for word, tag in tags)
    return counts

# wrapper to use the argument of terminal al the text file to be processed
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='Local Path for text file to be processed')
    args = parser.parse_args()
    with open('output3.txt', 'r') as f:
        text = f.read()
        c = count_verbs_nouns(text)
        print(c['NN'], 'nouns')
        print(c['VB'], 'verbs')