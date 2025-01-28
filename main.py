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


def rearrange_dict(dict):
    char_list = []  # Create a list instead of a dict
    for k in dict:
        if k.isalpha():  # Only include letters
            # Append a new dictionary for each character
            char_list.append({"character": k, "num": dict[k]})
    return char_list

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    number_of_words = count_words(file_contents)
    number_of_characters = count_characters(file_contents)
    # rearranging the dictionary
    numbers = rearrange_dict(number_of_characters)
    numbers.sort(reverse=True, key=sort_on)
    # printing report 
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print()

    for number in numbers:
        print(f"The '{number["character"]}' character was found {number["num"]} times")
    print("--- End report ---")
    










main()