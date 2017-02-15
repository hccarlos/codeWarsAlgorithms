# Take 2 strings s1 and s2 including only letters from a to z.
# Return a new sorted string, the longest possible, containing distinct letters,
# - each taken only once - coming from s1 or s2.
#
# Examples:
#
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    final_str = ""
    for char in s1:
        if char not in final_str:
            final_str += char
    for char in s2:
        if char not in final_str:
            final_str += char
    return "".join(sorted(final_str))

a = "abcdefghijklmnopqrstuvwxyz"
print longest(a, a)
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print longest(a, b)
