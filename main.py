import os

with open('books/frankenstein.txt') as infile:
    book_contents = infile.read()

print(book_contents)