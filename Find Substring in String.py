main_string = "Hello, world!"
substring = "world"

if substring in main_string:
    print(f"'{substring}' is found in '{main_string}'.")
else:
    print(f"'{substring}' is not found in '{main_string}'.")



import re

main_string = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"

match = re.search(pattern, main_string)

if match:
    print(f"Pattern '{pattern}' found at index {match.start()}.")
else:
    print(f"Pattern '{pattern}' not found.")


