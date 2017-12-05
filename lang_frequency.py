import sys
import re
from collections import Counter


def load_data(filepath):
    with open(filepath) as file_handler:
        text_object = file_handler.read()
    return text_object


def get_most_frequent_words(text_object):
    words = text_object.lower()
    all_words = re.findall(r'\w+', words)
    ten = 10
    most_frequent_words = Counter(all_words).most_common(ten)
    return most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 lang_frequency.py <path_to_txt>")
    filepath = sys.argv[1]
    file_object = load_data(filepath)
    hh = get_most_frequent_words(file_object)
    print("The most popular words:")
    print("-----------------------")
    for number, words_and_amount in enumerate(hh, 1):
        print("{} \t {} \t {}".format(number, *words_and_amount))
    print("_______________________")