
def two_sum(nums : list[int], target : int) -> list[int]:
    diffs = {int : int}
    k = 0
    for i in range(len(nums)):

        if diffs.get(target - nums[i], -1) == -1:
            diffs[nums[i]] = i
            continue
        
        k = i
        break

    return [diffs[target-nums[k]], k]

if __name__ == "__main__":
    test = [4,5,6]
    targ = 10
    print(two_sum(test, targ))