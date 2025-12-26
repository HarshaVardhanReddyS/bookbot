from stats import get_book_text, count_chars
import sys
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # words = get_book_text("./books/frankenstein.txt")
    for num in range(1, len(sys.argv)):
        words = get_book_text(sys.argv[num])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[num]}...")
        print("----------- Word Count ----------")
        print(words)
        print("--------- Character Count -------")
        chars = count_chars(sys.argv[num])
        if chars is not None:
            for char in chars:
                print(f'{char["name"]}: {char["num"]}')
        print("============= END ===============")
main() 