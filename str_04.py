def reverse_string(s):
    return s[::-1]

def count_characters(s):
    return {char: s.count(char) for char in set(s)}

def replace_character(s, old, new):
    return s.replace(old, new)

input_string = input("Enter a string: ")

print("Reversed String:", reverse_string(input_string))
print("Character Count:", count_characters(input_string))

old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")
print("Modified String:", replace_character(input_string, old_char, new_char))
