"""Change
 
https://exercism.org/tracks/python/exercises/change
"""

def find_fewest_coins(coins: list[int], change_target: int) -> list[int]:
    """Return the fewest number of coins equal to the `change_target`.
    
    :param coins: - The available coins' values.
    :param change_target: - The total change to be returned to the customer.
    :return change: - The appropriate change in the fewest number of coins.
    """
    if change_target < 0:
        raise ValueError("target can't be negative")
        
    dp = [float('inf')] * (change_target + 1)
    dp[0] = 0
    
    for coin in coins:
        for amount in range(coin, change_target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
            
    if dp[change_target] == float('inf'):
        raise ValueError("can't make target with given coins")
        
    change, amount = [], change_target
    while amount > 0:
        coin = next(c for c in coins if amount >= c and dp[amount] == dp[amount - c] + 1)
        change.append(coin)
        amount -= coin
        
    return change
  
