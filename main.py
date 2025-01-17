def main():
    book_path = "books/frankenstein.txt"   
    text = get_book_text(book_path)
    num_words = get_num_words(text)     #total number of words
    character_count = get_char_count(text)  # total number of alphabet characters only
    sorted_list = sort_count(character_count)

    print(f"--- Begin report of {book_path} --- ") #Prints report title
    print(f"{num_words} words were found in the document\n") #prints number of words
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"The '{char}' charcter was found {count} times")
    print("--- End report ---")


def get_char_count(text):
    char_dict = {}
    lowercase_text = text.lower()
    
    for character in lowercase_text:   
        if character.isalpha() == True: # check if it's a letter
            if character not in char_dict:  # add it to dict
                char_dict[character] = 1
            else:
                char_dict[character] += 1   # add to counter
        

    # Convert dictionary to list of dictionaries
    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    return char_list

def sort_on(char_list):
    return char_list["num"] # returns the value of the "num" in the dictionary

def sort_count(char_list):

    char_list.sort(reverse=True, key=sort_on) # sorts the characters
    return char_list

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
