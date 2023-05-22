class Vehicle:

  def __init__(self, make, model):
    self.make = make
    self.model = model

  def set_vehicle_make(self, make):
    self.make = make

  def set_vehicle_model(self, model):
    self.model = model

  def get_vehicle_make(self):
    return self.make

  def get_vehicle_model(self):
    return self.model


class Car(Vehicle):

  def __init__(self, make, model, doors):
    super().__init__(make, model)
    self.doors = doors

  def set_car_doors(self, doors):
    self.doors = doors

  def get_car_doors(self):
    return self.doors


class Pickup(Vehicle):

  def __init__(self, make, model, bed_length):
    super().__init__(make, model)
    self.bed_length = bed_length

  def set_bed_length(self, bed_length):
    self.bed_length = bed_length

  def get_bed_length(self):
    return self.bed_length


garage = []

while True:
  print("1. Add a car to virtual garage")
  print("2. Add a pickup truck to virtual garage")
  print("3. List vehicles in virtual garage")
  print("4. Quit")
  choice = int(
    input("Enter your choice as a number (1 for car, 2 for truck): "))

  if choice == 1:
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    doors = int(input("Enter number of doors: "))
    car = Car(make, model, doors)
    garage.append(car)
  elif choice == 2:
    make = input("Enter truck make: ")
    model = input("Enter truck model: ")
    bed_length = float(input("Enter bed length: "))
    pickup = Pickup(make, model, bed_length)
    garage.append(pickup)
  elif choice == 3:
    for i, vehicle in enumerate(garage):
      print(
        f"Vehicle {i + 1}: {vehicle.get_vehicle_make()} {vehicle.get_vehicle_model()}"
      )
      if isinstance(vehicle, Car):
        print(f"Doors: {vehicle.get_car_doors()}")
      elif isinstance(vehicle, Pickup):
        print(f"Bed Length: {vehicle.get_bed_length()}")
  elif choice == 4:
    break
  else:
    print("Invalid choice, try again.")
