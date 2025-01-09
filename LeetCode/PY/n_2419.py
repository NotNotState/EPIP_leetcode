def longest_subarray(nums: list[int]) -> int:
    # a AND b <= max(a,b) => max(nums) must be in the solution
    k, res, cnt = max(nums), 0, 0
    for elem in nums:
        if elem == k:
            cnt +=1
        else:
            cnt = 0
        res = max(cnt, res)

    return res

if __name__ == "__main__":
    test = [1,2,3,4]
    res = longest_subarray(test)
    print(res)

    
