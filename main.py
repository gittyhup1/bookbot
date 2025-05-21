
from stats import num_words, count_chars, format_char
import sys

# Check if we have the right number of arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# If we get here, sys.argv has exactly two elements
# so sys.argv[1] will be your book path
book_path = sys.argv[1]
# Rest of your code...

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(book_path)
    word_count = num_words(book_text)  # Call the function with the text
    print(f"{word_count} words found in the document")

    char_dict = count_chars(book_text)
    print(char_dict)

    formatted_report = format_char(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dic in formatted_report:
        if dic['char'].isalpha(): 
            print(f"{dic['char']}: {dic['num']}")
    print("============= END ===============")

main()
