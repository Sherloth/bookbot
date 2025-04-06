# get text from file an string
def get_book_text(book_path):
    with open(book_path) as f:
        content = f.read()
    return content

# create a list of strings
def word_count(book_path):
    text = get_book_text(book_path)
    split_list = text.split()
    return len(split_list)

# create dictionary of lowercase letter counts
def letter_count(book_path):
    new_list = list(get_book_text(book_path))
    dictionary = {}
    for letter in list(new_list):
        letter = letter.lower()
        if letter.isalpha():
            if letter not in dictionary:
                dictionary[letter] = 1
            elif letter in dictionary:
                dictionary[letter] += 1
    return dictionary

# dictionary of characters
def characters_dictionary(book_path):
    d_in = letter_count(book_path)
    d_out = []
    for char, count in d_in.items():
        d_out.append({"char": char, "count" : count})
    d_out.sort(key=lambda x: x["count"], reverse=True)
    return d_out