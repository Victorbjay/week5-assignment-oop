# Week 5 Assignment
# ================================
# Assignment 1: Design Your Own Class 🏗️

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")
    
    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu
    
    def play_game(self, game):
        print(f"🎮 Playing {game} on {self.brand} {self.model} with GPU {self.gpu}!")

# Test Assignment 1
phone1 = Smartphone("Samsung", "S23", 256)
phone1.info()
phone1.call("+123456789")

gaming_phone = GamingPhone("Asus", "ROG 7", 512, "Adreno 740")
gaming_phone.info()
gaming_phone.play_game("Call of Duty Mobile")


# ================================
# Assignment 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water...")

# Polymorphism Demo
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
