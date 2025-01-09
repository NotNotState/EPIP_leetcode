from collections import Counter

def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    
    temp = s1 + " " + s2
    words = temp.split()
    hashmap = dict.fromkeys(words, 0)
    res = set(words)
    doubles = set()

    for word in words:
        hashmap[word] += 1
        if hashmap[word] > 1:
            doubles.add(word)
    
    return res - doubles

def uncommonFromSentences_v2(s1: str, s2: str) -> list[str]:
    temp = s1 + " " + s2
    words = temp.split()

    hashmap = Counter(words)

    sol = [word for word in hashmap if hashmap[word] == 1]

    return sol


if __name__ == "__main__":
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    #s1 = "apple apple"
    #s2 = "banana"

    print(uncommonFromSentences_v2(s1, s2))

    