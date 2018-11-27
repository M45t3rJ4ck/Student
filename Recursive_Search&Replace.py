# Bonus task 2:
# Implement a search/replace function recursively
# Sample I/O
# Enter string: hello world
# Enter word to find: llo
# Enter word to replace: @@
# he@@ world
string = str(input("Enter a string for manipulation: "))
search = str(input("Enter the word to replace: "))
replace = str(input("Enter the replacement character: "))


def search_replace(string, search, replace):
    if search in string:
        return string.replace(search, replace)
    else:
        return str("no word found")


print(search_replace(string, search, replace))
