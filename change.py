CHANGE = 100
COINS = [1, 5, 10, 25, 50]              # dollar coins
# COINS = [1, 2, 5, 10, 20, 50, 100]      # euro coins


def count_change(change: int, coins: list[int]) -> int:
    # succes als change = 0
    # onmogelijk als change < 0 of coins = []
    # doorgaan zonder/gebruik eerste muntsoort
    pass


if __name__ == "__main__":
    print(
        f"""Wisselgeld van {CHANGE} is met de munten {COINS} """
        f"""op {count_change(CHANGE, COINS)} manieren te realiseren"""
    )
