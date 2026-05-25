class Plant:
    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age_days} days old")

    def __init__(self, name, height, age_days):
        self.name = name
        self._height = float(height)
        self._age_days = age_days

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

    def age(self):
        self._age_days += 1


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
        self.trunk_diameter =  float(trunk_diameter)
        self._shade = False

    def produce_shade(self):
        self._shade = True

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")
        if self._shade:
            print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

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



if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("=== Tree")
    tree = Tree("Oak", 200, 320, 15)
    tree.show()
    tree.produce_shade()
    tree.show()
    print("=== Vegetable")
    patato = Vegetable("Patato", 12, 8, "April")
    patato.show()
    for i in range(20):
        patato.grow()
        patato.age()
    patato.show()
    
    