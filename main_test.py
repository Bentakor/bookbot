def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
    return content

def main():
    print(get_book_text("books/frankenstein.txt"))

main()

