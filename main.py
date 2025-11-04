from stats import get_num_words
from stats import get_count_by_char
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(get_book_text(book_path))
    print("--------- Character Count -------")
    get_count_by_char(get_book_text(book_path))
    print("============= END ===============")

main()
