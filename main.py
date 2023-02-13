def how_many_letters_of_each_letter_in_alphabet_are_in_a_string(string):
  # the name of this method cannot be more explicit XD
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabet_count = {}
  for letter in alphabet:
    upper_letter = letter.upper()
    upper_letter_count = string.count(upper_letter)
    lower_letter_count = string.count(letter)
    alphabet_count[letter] = lower_letter_count + upper_letter_count
  return alphabet_count

def print_report(alphabet_count):
  print(f"Letter\tCount\n{13 * '.'}")
  for letter, count in alphabet_count.items():
    print(f"{letter}\t{count}")

with open("./books/frankenstein.txt") as file:
  file_contents = file.read()
  letters_count = 0
  for letter in file_contents:
    if letter.isalpha():
      letters_count += 1
  underscore_separator = len(str(letters_count)) + 25
  print(f"This document has {letters_count} words.\n{underscore_separator * '-'}\n")
  print_report(how_many_letters_of_each_letter_in_alphabet_are_in_a_string(file_contents))



# the method string.count() returns the number of times a letter appears in a string
