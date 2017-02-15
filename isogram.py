# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.
# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

def is_isogram(string):
    alpha = []
    for char in string:
        if char.lower() in alpha:
            return False
        else:
            alpha.append(char.lower())
    return True

print is_isogram("moOse")
print is_isogram("aba")
print is_isogram("Dermatoglyphics")
