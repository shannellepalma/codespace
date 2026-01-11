# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using bottom-up dynamic programming.

    :param weights: List of item weights
    :param values: List of item values
    :param capacity: Maximum weight capacity of the knapsack
    :return: Maximum value achievable
    """
    n = len(values)

    # Input validation
    if n == 0 or capacity <= 0:
        return 0
    if len(weights) != n:
        raise ValueError("weights and values lists must have the same length")
    if any(w < 0 for w in weights) or any(v < 0 for v in values):
        raise ValueError("weights and values must be non-negative")

    # DP table: (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: Include the item
                include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Option 2: Exclude the item
                exclude_item = dp[i - 1][w]
                # Take the better option
                dp[i][w] = max(include_item, exclude_item)
            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example usage
if __name__ == "__main__":
    try:
        # Example data
        values = [60, 100, 120]   # Item values
        weights = [10, 20, 30]    # Item weights
        capacity = 50             # Knapsack capacity

        max_value = knapsack(weights, values, capacity)
        print(f"Maximum value achievable: {max_value}")

    except ValueError as e:
        print(f"Error: {e}")
