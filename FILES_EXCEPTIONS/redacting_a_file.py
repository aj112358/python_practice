# Exercise 169: Redacting Text in a File
# Redact sensitive words.
# List of sensitive words provided in another file.

import sys

if len(sys.argv) < 4:
    print("Not enough command line arguments. Please try again.")
    quit()


