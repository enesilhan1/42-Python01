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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-10)
    rose.set_age(-5)
    print("Current state: ", end= "")
    rose.show()

