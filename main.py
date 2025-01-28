def count_words(book_to_count):
    list_with_words = book_to_count.split()
    
    return len(list_with_words)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    number_of_words = count_words(file_contents)
    print(number_of_words)
    










main()