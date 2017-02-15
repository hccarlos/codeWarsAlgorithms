# Your task is to make a function that can take any non-negative integer as argument
# and return it with it's digits in descending order.
# Examples:
# Input: 145263 Output: 654321
# Input: 1254859723 Output: 9875543221

def sortDigits(num):
    num_list = []
    while num:
        num_list.append(str(num % 10))
        num //= 10
    num_list.sort(key=int, reverse=True)
    s = '0' + "".join(num_list)
    return int(s)


print sortDigits(0)
