from itertools import permutations


def main() -> None:
    digits = list(range(10))
    answer = "".join(map(lambda x: str(x), list(permutations(digits))[999999]))
    print(answer)


if __name__ == "__main__":
    main()
