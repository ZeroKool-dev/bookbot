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

def count_words(text):
    """
    Counts the number of words in a given text.

    Parameters:
        text (str): The input text.

    Returns:
        int: The word count.
    """
    words = text.split()
    return len(words)

def main():
    """
    Uses get_book_text to read the contents of 'frankenstein.txt'
    and prints it to the console.
    """
    filepath = 'books/frankenstein.txt'  # Example relative path
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")


if __name__ == '__main__':
    main()