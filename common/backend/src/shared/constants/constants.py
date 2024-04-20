from datetime import timezone


UTC: timezone = timezone.utc


if __name__ == "__main__":
    from datetime import datetime

    print(UTC)
    print(type(UTC))
    print(datetime.now(UTC))
    print(datetime.now().astimezone(UTC))
