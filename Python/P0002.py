from typing import Generator


def fibonacci(value: int) -> Generator[int, None, None]:
    sequence = {0: 1, 1: 1}
    count = 0
    while sequence[list(sequence)[-1]] < value:
        if count not in sequence:
            sequence[count] = sequence[count - 1] + sequence[count - 2]
        yield sequence[count]
        count += 1


def is_even(number: int) -> bool:
    return number & 1 == 0


def main() -> None:
    answer = sum(filter(is_even, fibonacci(4000000)))
    print(f"Answer: {answer}")


if __name__ == '__main__':
    main()
