def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

from stats import count_words

from stats import word_counter

from stats import sorting

def main():
    content = get_book_text("books/frankenstein.txt")
    chars = word_counter(content)
    sorted_chars = sorting(chars)
    file_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(count_words(content))
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



main()