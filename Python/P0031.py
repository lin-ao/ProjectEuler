#Calculating coefficient from polynomial function from generating function
def count_combinations(coins: list[int], goal: int) -> int:
    coefficients = [0 for _ in range(goal + 1)]
    coefficients[0] = 1
    for coin in coins:
        for index in range(goal - coin + 1):
            coefficients[index + coin] += coefficients[index]
    return coefficients[-1]


def main() -> None:
    goal = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    answer = count_combinations(coins, goal)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
