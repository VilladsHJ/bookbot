def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    words = word_count(text)
    #print(text)
    #print(f"{words} words in the text")
    #print(character_counter(text))
    book_report(book_path, text, words)
    #char_sorter(text)
# Function that takes a path to a book text and returns the text
def book_text(path):
    with open(path) as f:
        return f.read()

# Function that takes a text string and returns the number of words in the string
def word_count(text_string):
    words = text_string.split()
    return len(words)

# Function that takes a text string and returns a dictionary with a count of each unique character in the text
def character_counter(text):
    character_counter = {}
    for char in text.lower():
        if char in character_counter:
            character_counter[char] += 1
        else:
            character_counter[char] = 1
    return character_counter

def char_sorter(text):
    sorted_list = []
    sorted_dictionary ={}
    for k in character_counter(text):
        sorted_list.append((character_counter(text)[k],k))
    sorted_list = sorted(sorted_list, reverse=True)
    for i in range(0,len(sorted_list)):
        sorted_dictionary[sorted_list[i][1]] = sorted_list[i][0]
    return sorted_dictionary

def book_report(book_path, text, count):
    final_dict = char_sorter(text)
    print(f"___ Report for {book_path} ___")
    print(f"The text contains {count} words")

    for k in final_dict:
        if final_dict[k] == 1:
            print(f"{k} is found {final_dict[k]} time")
        else:
            print(f"{k} is found {final_dict[k]} times")

main()

    