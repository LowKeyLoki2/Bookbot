
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(path):
    with open(path, "r") as file:
        text = file.read()
    return text

def word_count(path):
    book_text = get_book_text(path)
    book_text_split = book_text.split()
    word_count = len(book_text_split)
    return word_count


def get_character_count(path):
    book_text = get_book_text(path)
    book_text_lower = book_text.lower()
    character_count = {}
    for letters in book_text_lower:
        if letters in character_count:
            character_count[letters] += 1
        else: 
            character_count[letters] = 1
        
    return(character_count)



def sort_character_count(path):
    character_count = get_character_count(path)

    char_list = []
    for char, num in character_count.items():
        char_list.append({"char": char, "num": num})
    
    def sort_on(dict):
        return dict["num"]
    char_list.sort(key=sort_on, reverse=True)
    return char_list