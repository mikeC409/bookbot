import string

def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = count_words(file_contents)
    char_count = count_chars(file_contents)
    report = generate_report(file_contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{report['Word Count']} words found in the document\n")

    for letter, count in report['Letter Counts']:
        if count > 0:
            print(f"The '{letter}' character was found {count} times")

    print("--- End Report")

    # print(file_contents) testing the get_book_text function
    # print(f"{num_words} words found in the document") testing the count_words function
    # print(char_count) testing the count_chars function

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_chars(string):
    counts = {}
    text = string.lower()

    # Valid characters (letters)
    letters = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char in letters:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    return counts

def generate_report(string):
    letter_counts = count_chars(string)
    word_count = count_words(string)

    def get_count(item):
        return item[1]

    sorted_letter_counts = sorted(letter_counts.items(), key=get_count, reverse=True)

    report = {
        "Word Count": word_count,
        "Letter Counts": sorted_letter_counts
    }

    return report
    

main()