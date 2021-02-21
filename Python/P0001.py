def check_multiples(number: int) -> bool:
    return number % 3 == 0 or number % 5 == 0


def main() -> None:
    answer = sum(filter(check_multiples, range(1000)))
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
