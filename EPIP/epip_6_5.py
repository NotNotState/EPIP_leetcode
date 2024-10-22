def is_palindrome(stringy: str) -> bool:
    """
    Doesn't handle non-alphanumeric cases
    """
    #return all(stringy[i] == stringy[~i] for i in range(len(stringy)//2))
    return all(stringy[i] == stringy[-(i+1)] for i in range(len(stringy)//2))

def is_palindrome_v2(s : str) -> bool:

    i,j = 0, len(s)-1
    
    while i < j:

        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False
        
        i,j = i + 1, j - 1
    
    return True


def is_palindrome_pythonic(s : str) -> bool:

    return all (
        a == b 
        for a,b in zip(map(str.lower, filter(str.isalnum, s)), map(str.lower, filter(str.isalnum, reversed(s))))
    )

if __name__ == "__main__":
    test = "aaa***bbba!!!aa"
    test2 = "hallah"

    #print(is_palindrome_v2(test))
    #print(is_palindrome_pythonic(test))
    res = zip((map(str.lower, filter(str.isalnum, test2))),map(str.lower, filter(str.isalnum, reversed(test2))))
    print(list(res))