# Python 3.10 introduced the match statement, which is similar to the switch statement found in other programming languages.
# The basic syntax of the match statement involves matching a variable against several cases using the case keyword.


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status



# more :-


# New operators | and |= allow for merging and updating dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}




# You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager
'''
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
     # Process files
'''