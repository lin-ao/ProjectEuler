def load_input(path: str) -> list[int]:
    with open(path, "r") as f:
        for line in f:
            yield int(line)

def main() -> None:
    answer = sum(load_input("../Input/P0013.txt"))
    print(f"Answer: {str(answer)[:10]}")


if __name__ == "__main__":
    main()
