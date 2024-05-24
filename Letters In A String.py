def find_max_min_letters(input_string):
    max_letter = max(input_string, key=lambda x: ord(x))
    min_letter = min(input_string, key=lambda x: ord(x))
    return max_letter, min_letter

input_string =str(input( "Enter a string: "))
max_letter, min_letter = find_max_min_letters(input_string)
print(f"The maximum letter in the string is: {max_letter}")
print(f"The minimum letter in the string is: {min_letter}")