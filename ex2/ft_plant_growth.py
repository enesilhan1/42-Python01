class Plant:
    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age_days} days old")

    def age(self):
        self.age_days = self.age_days + 1

    def grow(self):
        self.height = self.height + 0.8


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 15
    rose.age_days = 25
    start_height = rose.height
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")
