class Plant:
    def show(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age_days} days old")

    def __init__(self, name, height, age_days):
        self.name = name
        self.height = float(height)
        self.age_days = age_days


if __name__ == "__main__":
    rose = Plant("Rose", 15, 25)
    cactus = Plant("Cactus", 66, 52)
    daisy = Plant("Daisy", 12, 20)
    patato = Plant("Patato", 12, 14)
    cabbage = Plant("Cabbage", 16, 21)

    print("=== Plant Factory Output ===")

    rose.show()
    cactus.show()
    daisy.show()
    patato.show()
    cabbage.show()
