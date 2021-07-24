def gen_corner(start: int, stride: int) -> list[int]:
    return [start + num * stride for num in range(1, 5)]


def sum_diag(side: int) -> int:
    total = 0
    position = 1
    for num in range(2, side, 2):
        if num < side:
            corners = gen_corner(position, num)
            total += sum(corners)
            position = corners[-1]
    return total + 1


def main() -> None:
    assert sum_diag(5) == 101
    answer = sum_diag(1001)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
