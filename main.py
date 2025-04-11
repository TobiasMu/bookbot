from stats import count_words, count_symbols, report
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        txt = f.read()
    return txt 


def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    string =get_book_text(path_to_book)
    word_count = count_words(string)
    another_fstring = f"Found {word_count} total words"
    print(another_fstring)
    # print(count_symbols(string))

    list_of_dicts = (report(count_symbols(string)))
    for dict in list_of_dicts:
        fstring = f"{dict["symbol"]}: {dict["count"]}"

        print(fstring) 

main()
