class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = int(rooms)
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}, Plot: {self.plot}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: Area: {self.area}, Rooms: {self.rooms}, Price: {self.price}, Address: {self.address}, Floor: {self.floor}"

house1 = House(120, 5, 300000, "123 Main St", 500)
flat1 = Flat(80, 3, 200000, "456 Elm St", 2)

print(house1)
print(flat1)