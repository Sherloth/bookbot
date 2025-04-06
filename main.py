# imports
from stats import word_count, characters_dictionary

book_path = "books/frankenstein.txt"

# define main function - print text stating the amount of words
def main():
    num_words = word_count()
    dictionary = characters_dictionary()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dictionary:
        print(f"{item["char"]} : {item["count"]}")
    

# call function
main()


