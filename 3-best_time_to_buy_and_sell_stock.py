# You are given an array prices where prices[i] is the price of a given stock on day i. You want to maximize your profit by choosing a single day to buy a stock and choosing a different day in the future to sell that stock.

# prices = [7,1,5,3,6,4]

# | day | price | cheapest so far | profit if sold today | best profit so far |
# | 0 | 7 | 7 | 0 | 0 |
# | 1 | 1 | 1 | 0 | 0 |
# | 2 | 5 | 1 | 4 | 4 |
# | 3 | 3 | 1 | 2 | 4 |
# | 4 | 6 | 1 | 5 | 5 |
# | 5 | 4 | 1 | 3 | 5 |


def max_profit(prices: list[int]) -> int:
    # Write your code here

    # initialize your tracking variables here
    cheapest_so_far: int = prices[0]
    best_profit_so_far: int = 0

    for price in prices:
        # update cheapest so far
        cheapest_so_far = min(cheapest_so_far, price)

        # update best profit so far
        profit_if_sold_today = price - cheapest_so_far
        best_profit_so_far = max(best_profit_so_far, profit_if_sold_today)

    return best_profit_so_far
