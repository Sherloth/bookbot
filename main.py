# imports
from stats import word_count
from stats import letter_count

book_path = "books/frankenstein.txt"

# define main function - print text stating the amount of words
def main():
    num_words = word_count()
    dictionary = letter_count()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(f"{dictionary}")
    

# call function
main()


