def print_spiral(matrix, rows, cols):
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        # Print top row
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        # Print right column
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        # Print bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

  
      # Print left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1

if __name__ == "__main__":
    rows = int(input())
    cols = int(input())
    matrix = []

    # Input matrix elements
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Print spiral elements
    print_spiral(matrix, rows, cols)