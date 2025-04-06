# get text from file an string
def get_book_text():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        content = f.read()
    return content

# create a list of strings
def word_count():
    text = get_book_text()
    split_list = text.split()
    return len(split_list)

# create dictionary of lowercase letter counts
def letter_count():
    new_list = list(get_book_text())
    dictionary = {}
    for letter in list(new_list):
        letter = letter.lower()
        if letter not in dictionary:
            dictionary[letter] = 1
        elif letter in dictionary:
            dictionary[letter] += 1
    return dictionary
