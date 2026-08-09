def remove_fourth_character(word: str) -> str:
    first_three_chars = word[:3]
    word_minus_fourth_char = word[4:]
    return first_three_chars + word_minus_fourth_char


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
