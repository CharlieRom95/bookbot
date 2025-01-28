def count_words(book_to_count):
    list_with_words = book_to_count.split()
    
    return len(list_with_words)

def count_characters(book_to_count):
    new_dict = {}
    new_book_to_count = book_to_count.lower()
    for character in new_book_to_count:
        new_dict[character] = 0
    for character in new_book_to_count:
        new_dict[character] += 1
    return new_dict



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    number_of_characters = count_characters(file_contents)
    print(number_of_characters)
    










main()