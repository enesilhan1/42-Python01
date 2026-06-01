class Plant:
    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age_days} days old")
        self._stats._show_count += 1

    def __init__(self, name, height, age_days):
        self.name = name
        self._height = float(height)
        self._age_days = age_days
        self._stats = Plant.Stats()

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {height}cm")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age_days

    def set_age(self, age_days):
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = age_days
            print(f"Age updated: {age_days} days")

    def grow(self):
        self._height = round(self._height + 0.8, 1)
        self._stats._grow_count += 1

    def age(self):
        self._age_days += 1
        self._stats._age_count += 1

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)

    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self):
            print(
                f"Stats: {self._grow_count} grow,"
                f"{self._age_count} age, {self._show_count} show"
            )


def display_stats(plant):
    plant._stats.display()


class Flower(Plant):
    def __init__(self, name, height, age_days, color):
        super().__init__(name, height, age_days)
        self.color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age_days, trunk_diameter):
        super().__init__(name, height, age_days)
        self.trunk_diameter = float(trunk_diameter)
        self._shade = False
        self._shade_count = 0

    def produce_shade(self):
        self._shade = True
        self._shade_count += 1

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")
        if self._shade:
            print(
                f"Tree {self.name} now produces a shade of"
                f"{self._height}cm long and {self.trunk_diameter}cm wide."
            )


class Vegetable(Plant):
    def __init__(self, name, height, age_days, harvest_season):
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self):
        super().grow()
        self._nutritional_value += 1

    def age(self):
        super().age()

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name, height, age_days, color):
        super().__init__(name, height, age_days, color)
        self._seed_count = 0

    def bloom(self):
        super().bloom()
        self._seed_count = 42

    def show(self):
        super().show()
        print(f" Seeds: {self._seed_count}")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print(f"[statistics for {rose.name}]")
    rose._stats.display()
    for i in range(10):
        rose.grow()
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose.name}]")
    rose._stats.display()

    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print(f"[statistics for {oak.name}]")
    oak._stats.display()
    print(f" {oak._shade_count} shade")
    oak.produce_shade()
    oak.show()
    print(f"[statistics for {oak.name}]")
    oak._stats.display()
    print(f" {oak._shade_count} shade")

    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    sunflower.bloom()
    for i in range(20):
        sunflower.grow()
        sunflower.age()
    sunflower.show()
    print(f"[statistics for {sunflower.name}]")
    sunflower._stats.display()

    print()

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print(f"[statistics for {unknown.name}]")
    unknown._stats.display()

    print()

    display_stats(rose)
    display_stats(oak)
