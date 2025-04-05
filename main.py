# get text from file an string
def get_book_text():
    with open("/home/amiansherloth/github.com/bootdev/bookbot/books/frankenstein.txt") as f:
        content = f.read()
    return content

# create a list of strings - words and count them
def word_count():
    text = get_book_text()
    split_list = text.split()
    count = 0

    # count strings with loop
    for word in split_list:
        count += 1
    return count

# define main function - print text stating the amount of words
def main():
    num_words = word_count()
    print(f"{num_words} words found in the document")

# call function
main()


