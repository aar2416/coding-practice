def adjust_prices(prices, k):
    """
    Adjusts the prices of items to have a median as close to k as possible.

    Args:
        prices: A list of integers representing the prices of items.
        k: The target median price.

    Returns:
        The minimum number of moves required to adjust the prices and the achieved median.
    """
    n = len(prices)
    prices.sort()
    median_index = (n - 1) // 2 + 1
    moves = 0

    # Loop until no further adjustments are possible in a single pass
    for i in range(0, median_index):
        if prices[i] > k and i <= median_index:
            moves += (prices[i] - k)
            # if prices[i] 
            prices[i] = prices[i] - (prices[i] - k)
        elif prices[i] < k and i > median_index:
            moves += (k - prices[i])
            prices[i] += (k - prices[i])
    
    # Calculate the median of the adjusted prices (closest achievable median)
    achieved_median = prices[median_index]
    return moves, achieved_median

# Example usage
prices = [6, 2, 1, 6, 6, 7]
# [1,2,4,4,4,7]
k = 2
min_moves, achieved_median = adjust_prices(prices.copy(), k)

print(f"Minimum number of moves required: {min_moves}")
print(f"Achieved median: {achieved_median}")