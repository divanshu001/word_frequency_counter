# WORD FREQUENCY COUNTER
import string
from collections import Counter


def process_text(text_file):  # this method will remove punctuations
    """The .maketrans() method here takes three arguments, the first two of which are empty strings,
    and the third is the list of punctuation we want to remove. This tells the function to replace all
    punctuation with None."""
    data = text_file.translate(str.maketrans('', '', string.punctuation)).lower()
    return data


def count_word_frequency(data):  # count frequency using counter
    """Counter is a sub-class that is used to count hashable objects. It implicitly creates a hash table of an
    iterable when invoked."""
    count = Counter(data.split())
    return count


def display_word_frequency(count):
    # sorted(iterable, key=key, reverse=reverse)
    dict1 = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print('Word Frequencies:')
    for keys, values in dict1:
        print(f"{keys} : {values}")  # formatted string


def main():
    # input file path from user
    file_path = input("Enter file path {text file} : ")
    try:
        with open(file_path, 'r') as read_file:
            text_file = read_file.read()
    except FileNotFoundError:
        print("No such file found")
        return
    # function call
    data = process_text(text_file)
    count = count_word_frequency(data)
    display_word_frequency(count)


if __name__ == '__main__':
    main()  # call main function
