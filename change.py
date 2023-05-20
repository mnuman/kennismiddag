CHANGE = 100
COINS = [1, 5, 10, 25, 50]


def count_change(change: int, coins: list[int]) -> int:
    # succes als change = 0 -> 1
    # onmogelijk als change < 0 of coins = [] -> 0
    # doorgaan zonder/gebruik eerste muntsoort -> recursie
    pass

if __name__ == "__main__":
    print(
        f"""Wisselgeld van {CHANGE} is met de munten {COINS} """
        f"""op {count_change(CHANGE, COINS)} manieren te realiseren"""
    )
