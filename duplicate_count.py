# Count the number of Duplicates
#
# Write a function that will return the count of
# distinct case-insensitive alphabetic characters and
# numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphanumeric characters,
# including digits, uppercase and lowercase alphabets.
#
# Example:
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabbcdeB" -> 2 # 'a' and 'b'
# "indivisibility" -> 1 # 'i'
# "Indivisibilities" -> 2 # 'i' and 's'
# "aa11" -> 2 # 'a' and '1'

def duplicate_count(text):
    dic = {}
    for char in text:
        char = char.lower()
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    new_dic = {key: val for key, val in dic.items() if val > 1}
    # print new_dic
    return len(new_dic)
print duplicate_count("Indivisibilities")
