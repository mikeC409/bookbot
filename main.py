def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = count_words(file_contents)
    char_count = count_chars(file_contents)
    print(file_contents)
    print(f"{num_words} words found in the document")
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_chars(text):
    counts = {}
    text = text.lower()

    # Valid characters (letters)
    letters = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char in letters:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    return counts

main()