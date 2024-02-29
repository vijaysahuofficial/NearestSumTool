def nearest_sum(numbers, target_sum):
    n = len(numbers)
    # Create a 2D array to store the possible sums
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            if j >= numbers[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - numbers[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # Find the nearest sum
    nearest = float('inf')
    for j in range(target_sum, -1, -1):
        if dp[n][j]:
            nearest = j
            break

    # Reconstruct the subset of numbers contributing to the nearest sum
    subset = []
    j = nearest
    for i in range(n, 0, -1):
        if j >= numbers[i - 1] and dp[i - 1][j - numbers[i - 1]]:
            subset.append(numbers[i - 1])
            j -= numbers[i - 1]

    return nearest, subset

def main():
    # Take user input for numbers and target sum
    numbers = list(map(int, input("Enter the list of numbers separated by commas: ").split(',')))
    target_sum = int(input("Enter the target sum: "))

    # Calculate nearest sum and subset
    nearest, subset = nearest_sum(numbers, target_sum)
    print("Nearest sum to", target_sum, "is:", nearest)
    print("Subset of numbers contributing to this sum:", subset)

if __name__ == "__main__":
    main()
