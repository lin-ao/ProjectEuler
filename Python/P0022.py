def load_input(path: str) -> list[str]:
    with open(path, "r") as f:
        return sorted([name.strip('"') for name in f.readline().rstrip("\n").split(",")])


def char_to_int(char: str) -> int:
    return ord(char) - 64


def string_to_int(string: str) -> int:
    return sum(char_to_int(char) for char in string)


def calculate_value(names: list[str]) -> int:
    return sum(index * string_to_int(name) for index, name in enumerate(names, 1))


def main() -> None:
    assert 938 * string_to_int("COLIN") == 49714
    names = load_input("../Input/P0022.txt")
    answer = calculate_value(names)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
        