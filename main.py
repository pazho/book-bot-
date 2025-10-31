def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

from stats import count_words

from stats import word_counter

def main():
    content = get_book_text("books/frankenstein.txt")
    chars = word_counter(content)
    print(count_words(content))
    print(chars)


main()