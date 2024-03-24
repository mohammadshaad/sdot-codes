def main():
    nums_str = input().split()
    nums_divide_str = input().split()
    nums = list(map(int, nums_str))
    nums_divide = list(map(int, nums_divide_str))
    print(min_operation(nums, nums_divide))

def min_operation(nums, nums_divide):
    g = nums_divide[0]
    for i in nums_divide:
        g = gcd(g, i)
    smallest = float('inf')
    for num in nums:
        if g % num == 0:
            smallest = min(smallest, num)
    if smallest == float('inf'):
        return '-1'

    min_op = 0
    for num in nums:
        if num > smallest:
            min_op += 2
    return str(min_op)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    main()

# def main():
#     nums = list(map(int, input().split()))
#     nums_divide = list(map(int, input().split()))
#     print(min_deletions(nums, nums_divide))

# def min_deletions(nums, nums_divide):
#     # Calculate the greatest common divisor of nums_divide
#     g = nums_divide[0]
#     for i in nums_divide:
#         g = gcd(g, i)
    
#     # Count distinct numbers in nums that are not divisible by g
#     distinct_nums = set(nums)
#     count = 0
#     for num in distinct_nums:
#         if num % g != 0:
#             count += 1
    
#     return count

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# if __name__ == "__main__":
#     main()
