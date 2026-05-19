class Plant:
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 15
    rose.age = 25
    rose.show()
    daisy = Plant()
    daisy.name = "Daisy"
    daisy.height = 12
    daisy.age = 20
    daisy.show()
    cactus = Plant()
    cactus.name = "Cactus"
    cactus.age = 52
    cactus.height = 66
    cactus.show()
