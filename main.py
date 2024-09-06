def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(num_words)
    letter_count = count_letters(text)
    for k, v in letter_count.items():
        print(k, ":", v)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    letters = sorted(" ".join(text.lower()).split())
    letter_count = {}
    for i in letters:
        if i in letter_count.keys():
            letter_count[i] += 1
        else:
            letter_count[i] =  1
    return letter_count
main()