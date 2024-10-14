def count_set_bits(a):
    cnt = 0
    if (a<0):
        a = abs(a)
        a = ~a + 1
        cnt += 1
    num_bit_len = a.bit_length()
    for i in range(num_bit_len):
        if (a&1):
            cnt += 1
        a >>= 1
    return cnt

x = int(input())
print(count_set_bits(x))