def my_bit_length(a):
    a =abs(a)
    counter = 0
    while (a != 0):
        counter += 1
        a >>= 1
    return counter
def count_set_bits(a, num_bit_len):
    cnt = 0
    if (a < 0):
        a = abs(a)
        a = ~a + 1
        cnt += 1
    while(num_bit_len > 0):
        if (a & 1):
            cnt += 1
        a >>= 1
        num_bit_len -=1
    return cnt
x = int(input())
print(count_set_bits(x, my_bit_length(x)))
# print(my_bit_length(x))
# print(x.bit_length())
assert count_set_bits(-123, my_bit_length(-123)) == 3, "Assert error"
assert count_set_bits(-512, my_bit_length(-512)) == 2, "Assert error"
assert count_set_bits(257, my_bit_length(257)) == 2, "Assert error"