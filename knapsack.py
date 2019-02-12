"""This script solves the 0:1 knapsack problem."""
from collections import namedtuple
from functools import lru_cache


def knapsack(items, maxweight):
    """Find the most valuable items that weigh no more than maxweight."""
    @lru_cache(maxsize=None)
    def bestvalue(i, j):
        """Return the value of the most valuable subsequence."""
        if j < 0:
            return float('-inf')
        if i == 0:
            return 0
        item = items[i - 1]
        return max(bestvalue(i - 1, j),
                   bestvalue(i - 1, j - item.weight) + item.value)

    j = maxweight
    result = []
    for ind, item in reversed(list(enumerate(items))):
        if bestvalue(ind + 1, j) != bestvalue(ind, j):
            result.append(item)
            j -= item.weight
    result.reverse()
    return bestvalue(len(items), maxweight), result


Item = namedtuple('Item', 'name weight value'.split())


ITEMS = [
    Item("map_", 9, 150),
    Item("compass", 13, 35),
    Item("water", 153, 200),
    Item("sandwich", 50, 160),
    Item("glucose", 15, 60),
    Item("tin", 68, 45),
    Item("banana", 27, 60),
    Item("apple", 39, 40),
    Item("cheese", 23, 30),
    Item("beer", 52, 10),
    Item("suntan_cream", 11, 70),
    Item("camera", 32, 30),
    Item("T_shirt", 24, 15),
    Item("trousers", 48, 10),
    Item("umbrella", 73, 40),
    Item("waterproof_trousers", 42, 70),
    Item("waterproof_overclothes", 43, 75),
    Item("note_case", 22, 80),
    Item("sunglasses", 7, 20),
    Item("towel", 18, 12),
    Item("socks", 4, 50),
    Item("book", 30, 10),
]


print(knapsack(ITEMS, 400))
