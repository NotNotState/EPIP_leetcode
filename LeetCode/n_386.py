
def lexicalOrderIterative(n: int) -> list[int]:
    res = []
    curr_num = 1

    for _ in range(n):
        print(curr_num)
        res.append(curr_num)

        if curr_num * 10 <= n:
            curr_num *= 10
        else:
            
            while curr_num % 10 == 9 or curr_num >= n:
                curr_num //= 10
            
            curr_num += 1


    return res

def lexicalOrderIterative2(n: int) -> list[int]:
    res = []
    curr = 1

    while len(res) < n:
        res.append(curr)
        if curr * 10 <= n: curr *= 10
        elif curr % 10 != 9 and curr + 1 <= n: curr += 1
        else:
            while (curr // 10) % 10 == 9:
                curr //= 10
            
            curr = (curr // 10) + 1
        
    
    return res





# Lexicographical Sorting on input n
if __name__ == "__main__":
    #n = 192
    #n = 2
    #n = 100
    n = 13
    print(lexicalOrderIterative2(n))


                

