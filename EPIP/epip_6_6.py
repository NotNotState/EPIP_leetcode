def reverse_sentence(sentence: str) -> str:

    def reverse(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start+1, finish-1

    reverse(sentence, 0, len(sentence)-1)

    start = 0
    while start < len(sentence):
        end = start

        while end < len(sentence) and sentence[end] != " ":
            end += 1

        # not sure if this need to be here, don't believe so given the while conditions
        #if end == len(sentence):
        #    break

        reverse(sentence, start, end-1)
        start = end + 1


if __name__ == "__main__":
    test = "Steve Buccemi is the greatest"
    test = [i for i in test]
    reverse_sentence(test)
    print(test)

