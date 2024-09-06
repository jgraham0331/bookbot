def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    letter_count = count_letters(text)
    letter_count.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("\n")

    for i in letter_count:
        print(f"The \'{i['character']}\' character was found {i['count']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    letters = sorted(" ".join(text.lower()).split())
    letters = [i for i in letters if i.isalpha()]
    letter_count = {}
    for i in letters:
        if i in letter_count.keys():
            letter_count[i] += 1
        else:
            letter_count[i] =  1
    return [{"character": k, "count": v} for k, v in letter_count.items()]

def sort_on(dict):
    return dict["count"]

main()