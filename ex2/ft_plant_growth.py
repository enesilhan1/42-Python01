class Plant:
    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, "
            f"{self._age_days} days old"
        )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self._height = height
        self._age_days = age_days

    def age(self) -> None:
        self._age_days += 1

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)


if __name__ == "__main__":
    rose = Plant("Rose", 15, 25)
    start_height = rose._height
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose._height - start_height, 1)}cm")
