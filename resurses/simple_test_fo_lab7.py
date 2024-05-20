from src.boyer_moore import *

haystack = "this is a simple example"
needle = "example"
result = boyer_moore(haystack, needle)
print("Індекс першого входження підстрічки:", result)