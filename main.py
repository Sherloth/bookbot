# imports
from stats import word_count, characters_dictionary
import sys

# sys.agrv check
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

# define main function - print text stating the amount of words
def main():
    num_words = word_count(book_path)
    dictionary = characters_dictionary(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dictionary:
        print(f"{item["char"]}: {item["count"]}")
    

# call function
main()

print("Hello")

