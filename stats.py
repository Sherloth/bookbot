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

