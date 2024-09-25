class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        max_ = 100000
        positions = [max_] * (amount + 1)
        positions[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    positions[i] = min(positions[i], positions[i - coin] + 1)
        res = positions[amount]
        return -1 if res == max_ else res
