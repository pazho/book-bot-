def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents


def count_words(content):
    word_count = content.split()
    words = len(word_count)
    return f"Found {words} total words"

def main():
    content = get_book_text("books/frankenstein.txt")
    print(count_words(content))

main()