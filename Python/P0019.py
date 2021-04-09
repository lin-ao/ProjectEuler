from datetime import datetime, timedelta


def dates(start_date: datetime, end_date: datetime) -> datetime:
    for i in range(int((end_date - start_date).days)):
        yield start_date + timedelta(i)


def is_sunday(date: datetime) -> bool:
    return date.weekday() == 1


def count_first_sunday(start_date: datetime, end_date: datetime) -> int:
    return sum(date.weekday() == 1 and date.day == 1 for date in dates(start_date, end_date))


def main() -> None:
    start_date = datetime(1901, 1, 1)
    end_date = datetime(2000, 12, 31)
    answer = count_first_sunday(start_date, end_date)
    print(f"Answer: {answer}")


if __name__ == "__main__":
    main()