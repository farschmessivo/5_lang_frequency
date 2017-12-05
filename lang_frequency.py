import sys
import re
import pprint
from collections import Counter


def load_data(filepath):
    words = re.findall(r'\w+', open(filepath).read().lower())
    return words


def get_most_frequent_words(words):
    most_frequent_words = Counter(words).most_common(10)
    return most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 lang_frequency.py <path_to_txt>")
    filepath = sys.argv[1]
    file_object = load_data(filepath)
    print('---------------------------')
    print('ten most popular words:')
    pprint.pprint(get_most_frequent_words(file_object))

