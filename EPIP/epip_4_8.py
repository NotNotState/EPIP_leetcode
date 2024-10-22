"""
First Two are from intro to chapter
"""
def parity_check_brute(x : int) -> int:
    result = 0
    while x:
        result ^= x & 1 # XOR current val with 1 and assign, checks right most bit (1 if 1, and 0 if not), and XORs this with result to flip it's bit
        x >>= 1 # right shit, and assign, or drop lowerst sig bit
    return result

def parity_check_fast(x : int) -> int:
    result = 0 

    while x: 

        result ^= 1
        x &= x - 1 # comes from bit trick: x & (x-1) = x with it's lowers SET bit eraesed => (00101100) & (00101100 - 1) = (00101100) & (00101011) = (00101000)
        # this allows us to drop any non-set bits in our iterations

# Reverse the passed integer
def integer_reverse_brute(x : int) -> int:
    res = ""
    str_x = str(x)

    for i in range(len(str_x)-1, -1, -1):
        res += str_x[i]

    return int(res)

def integer_reverse_v2(x: int) -> int:
    res, x_rem = 0, abs(x)

    while x_rem:
        res = res * 10 + x_rem % 10
        x_rem //= 10

    return res if x > 0 else -res

if __name__ == "__main__":
    test = 400235

    print(integer_reverse_brute(test))
    print(integer_reverse_v2(test))