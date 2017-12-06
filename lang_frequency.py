import sys
import re
from collections import Counter


def load_data(filepath):
    with open(filepath) as file_handler:
        text = file_handler.read()
    return text


def get_most_frequent_words(text):
    words = text.lower()
    all_words = re.findall(r'\w+', words)
    ten = 10
    ten_most_frequent_words = Counter(all_words).most_common(ten)
    return ten_most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 lang_frequency.py <path_to_txt>")
    filepath = sys.argv[1]
    text = load_data(filepath)
    ten_most_frequent_words = get_most_frequent_words(text)
    print("The most popular words:")
    print("-----------------------")
    for number, (word, amount) in enumerate(ten_most_frequent_words, 1):
        print("{} \t {} \t {}".format(number, word, amount))
    print("_______________________")