from math import lcm


def main() -> None:
    assert lcm(*range(1, 11)) == 2520
    answer = lcm(*range(1, 21))
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
