# Convert a string to a new string where each character in the new string is
# '(' if that character appears only once in the original string, or
# ')' if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
#
# Examples:
# "din" => "((("
# "recede" => "()()()"
# "Success" => ")())())"
# "(( @" => "))(("

def duplicate_encode(word):
    # keep a dictionary where key is character,
    # and value is location of character in the original word
    word = word.lower()
    final_word_list = []
    dictionary = {}
    # go through each character in word, keeping the index/location of the character
    for index, char in enumerate(word):
        print str(index) + "  " + char
        # if the character does not show up in dictionary
        if char not in dictionary:
            # add it to the dictionary, as well as the position
            dictionary[char] = index
            # put a ( at current location
            final_word_list.append("(")
        # if character does show up in dictionary
        else:
            # find the location of the first occurence, and substitute that with )
            print final_word_list
            final_word_list[dictionary[char]] = ")"
            # also update current location with )
            final_word_list.append(")")
    return "".join(final_word_list)
# print duplicate_encode("din")
# print duplicate_encode("Success")
