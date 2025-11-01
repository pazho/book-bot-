import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

from stats import count_words

from stats import word_counter

from stats import sorting

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    #lines = content.split("\n")
    #start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    #start_book = 0
    #end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
    #end_book = 0

    #for index, line_text in enumerate(lines):
        #if start_marker in line_text:
            #start_book = index
            #break
    
    #for index, line_text in enumerate(lines):
        #if end_marker in line_text:
            #end_book = index
            #break
    #book_lines = lines[start_book: end_book]
    #cleaned_content = "\n".join(book_lines)
    chars = word_counter(content)
    sorted_chars = sorting(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(count_words(content))
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



main()