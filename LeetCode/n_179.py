import functools

"""
Note on python cmp definitions:
a comparison function is any callable that accepts two arguments, compares them, and returns a negative number for less-than,
 zero for equality, or a positive number for greater-than. 
 A key function is a callable that accepts one argument and returns another value to be used as the sort key.

 Comparision functions and key functions for sorting
 link: https://learnpython.com/blog/python-custom-sort-function/#:~:text=Custom%20Comparison%20with%20Sort%20Function%20in%20Python&text=It%20will%20return%20a%20number,a%20negative%20number%3A%20x%20%3C%20y
 links: https://www.programiz.com/python-programming/methods/built-in/sorted
 """

def largestNumber(nums: list[int]) -> str:
    nums = list(map(str, nums))
    def cmp (x, y):
        return -1 if x + y > y + x else 1
    
    # need to use functools.cmp_to_key to convert cmp to key. cmp is the old formatting and less complexity efficient
    nums.sort(key=functools.cmp_to_key(cmp))
    sol = "".join(nums)

    return 0 if sol[0] == '0' else sol


if __name__ == "__main__":
    test = [2,30,34,59,9]
    #test = [3,30,34,59,9]
    #test = [3,30,34,5,9]
    print(largestNumber(test))