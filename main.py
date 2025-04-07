import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file_path = sys.argv[1]
from stats import how_many, characters_count, pretty
def main():
    with open(sys.argv[1]) as f:
        content = f.read()

    words = how_many(content)
    letters = characters_count(content)
    ordered = pretty(characters_count(content))
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book ")
    print(f"------------ Word Count ---------")
    print(f"Found {words} total words")
    print(f"--------- Character Count -------")
    for order in ordered:
        if order["letter"].isalpha():
            print(f"{order["letter"]}: { order["count"]}")
main()
