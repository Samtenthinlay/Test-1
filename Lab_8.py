def find_first_repeating_character(s):
  """
  Finds the first repeating character in a string and prints its memory address.

  Args:
      s: The input string.

  Returns:
      The first repeating character and its memory address, or None if no repeating character is found.
  """

  char_counts = {}
  for char in s:
    if char in char_counts:
      # Print the character and its memory address using f-string formatting
      print(f"First repeating character: {char} (memory address: {id(char)})")
      return char
    char_counts[char] = 1
  return None

# Example usage
string = "aabccdd"
first_repeating_char = find_first_repeating_character(string)

if first_repeating_char is None:
  print("No repeating character found")