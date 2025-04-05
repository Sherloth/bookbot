# imports
from stats import word_count

# define main function - print text stating the amount of words
def main():
    num_words = word_count()
    print(f"{num_words} words found in the document")

# call function
main()


