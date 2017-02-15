# Write a function called validParentheses that takes a string of parentheses,
# and determines if the order of the parentheses is valid.
# validParentheses should return true if the string is valid, and false if it's invalid.
#
# Examples:
# validParentheses( "()" ) => returns true
# validParentheses( ")(()))" ) => returns false
# validParentheses( "(" ) => returns false
# validParentheses( "(())((()())())" ) => returns true
#
# All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'

def valid_parentheses(str):
    # keep an array of parentheses
    left_paren_num = 0
    # increment left_paren_num if token from str is a (
    # decrement left_paren_num (if left_paren_num > 0) if token is a )
    for token in str:
        if token == '(':
            left_paren_num += 1
        elif token == ')':
            left_paren_num -= 1
        if left_paren_num < 0:
            return False
    return left_paren_num == 0

print valid_parentheses( "()" )
print valid_parentheses( ")(()))" )
print valid_parentheses( "(" )
print valid_parentheses( "(())((()())())" )
