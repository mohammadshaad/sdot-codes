def find_peak_index(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    # At the end, left and right will be equal
    return left
def main():
    n = int(input("Enter the length of the array: "))
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    peak_index = find_peak_index(arr)
    print("The peak index is:", peak_index)
if __name__ == "__main__":
    main()
