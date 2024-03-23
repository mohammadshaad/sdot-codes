def generate_permutations(nums, left, right):
    if left == right:
        # Base case: Print the current permutation
        print_array(nums)
    else:
        for i in range(left, right + 1):
            # Swap the current element with the element at index 'i'
            nums[left], nums[i] = nums[i], nums[left]
            # Recursively generate permutations for the remaining elements
            generate_permutations(nums, left + 1, right)
            # Backtrack: Undo the swap to restore the original order
            nums[left], nums[i] = nums[i], nums[left]

def print_array(nums):
    # Convert integers to strings before joining
    nums_str = [str(num) for num in nums]
    print(' '.join(nums_str))

if __name__ == "__main__":
    nums = input().split()
    n = len(nums)
    generate_permutations(nums, 0, n - 1)