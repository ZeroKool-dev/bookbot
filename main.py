from stats import get_num_words
from stats import get_num_characters
from stats import sort_char_count

def get_book_text(filepath):
    """
    Reads the contents of a text file and returns it as a string.

    Parameters:
        filepath (str): The path to the text file.

    Returns:
        str: The contents of the file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    """
    Uses get_book_text to read the contents of 'frankenstein.txt'
    and prints it to the console.
    """
    filepath = 'books/frankenstein.txt'  # Example relative path
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_char_count = sort_char_count(num_characters)
    print(f"Found {num_characters} total characters")
    print(f"Found {num_words} total words")
    print(sorted_char_count)


if __name__ == '__main__':
    main()