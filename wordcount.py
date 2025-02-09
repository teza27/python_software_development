statement = "The Lord of host is a good Lord , The Lord is mighty in deed"
def word_count(statement, *args):
    state_split = statement.split()
    print(state_split)
    word_dict = {}
    for char in args:
        word_number = state_split.count(char)
        word_dict[char] = word_number
    print(word_dict)
word_count(statement, "Lord", "host", "mighty", "deed", "The", "is")