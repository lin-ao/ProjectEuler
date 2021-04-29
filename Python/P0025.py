from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    sequence = {0: 1, 1: 1}
    count = 0
    while True:
        if count not in sequence:
            sequence[count] = sequence[count - 1] + sequence[count - 2]
        yield sequence[count]
        count += 1


def index_of_first_fibonacci_of_length(length: int) -> int:
    return next(index for index, number in enumerate(fibonacci(), 1) if len(str(number)) == length)


def main() -> None:
    assert index_of_first_fibonacci_of_length(3) == 12
    answer = index_of_first_fibonacci_of_length(1000)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
