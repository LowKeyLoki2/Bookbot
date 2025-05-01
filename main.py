import sys
from stats import word_count
from stats import get_character_count
from stats import sort_character_count

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



word_count_result = word_count(sys.argv[1])
sorted_chars = sort_character_count(sys.argv[1])

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_count_result} total words")
print("--------- Character Count -------")

# Loop through the sorted characters separately
for char_dict in sorted_chars:
    if char_dict["char"].isalpha():
        print(f"{char_dict['char']}: {char_dict['num']}")

print("============= END ===============")

        






