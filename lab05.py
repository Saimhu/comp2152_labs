# ----------------------------
# Question 1: Fibonacci (LeetCode #509)
# ----------------------------
def fib(n: int) -> int:
    """Return the nth Fibonacci number using recursion."""
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fib(n - 1) + fib(n - 2)


# ----------------------------
# Question 2: FizzBuzz (LeetCode #412)
# ----------------------------
def fizz_buzz(n: int) -> list[str]:
    """Return FizzBuzz list from 1..n."""
    result = []

    for i in range(1, n + 1):
        # Check BOTH first (important)
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


# ----------------------------
# Question 3: Binary Search (LeetCode #704)
# Part A: Iterative
# ----------------------------
def binary_search_iterative(nums: list[int], target: int) -> int:
    """Binary search using a while loop. Returns index of target, else -1."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# ----------------------------
# Question 3: Binary Search (LeetCode #704)
# Part B: Recursive
# ----------------------------
def binary_search_recursive(nums: list[int], target: int, left: int, right: int) -> int:
    """Binary search using recursion. Returns index of target, else -1."""
    # Base case: not found
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)


# ----------------------------
# Quick Tests (you can delete these if submission wants only functions)
# ----------------------------
if __name__ == "__main__":
    # Q1 Tests: fib 0..10
    print("Q1: Fibonacci tests (0..10)")
    for n in range(0, 11):
        print(f"fib({n}) = {fib(n)}")
    print()

    # Q2 Tests: fizzbuzz
    print("Q2: FizzBuzz tests")
    print("fizz_buzz(3)  =", fizz_buzz(3))
    print("fizz_buzz(5)  =", fizz_buzz(5))
    print("fizz_buzz(15) =", fizz_buzz(15))
    print()

    # Q3 Tests: binary search
    nums = [-1, 0, 3, 5, 9, 12]
    print("Q3: Binary Search tests")
    print("Array:", nums)

    target = 9
    print("Iterative search target 9:", binary_search_iterative(nums, target))
    print("Recursive search target 9:", binary_search_recursive(nums, target, 0, len(nums) - 1))

    target = 2
    print("Iterative search target 2:", binary_search_iterative(nums, target))
    print("Recursive search target 2:", binary_search_recursive(nums, target, 0, len(nums) - 1))
