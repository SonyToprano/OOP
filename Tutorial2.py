
#Tutorial 2: class variables

class House:
    location = 'Berceni'
    no_of_houses = 0
    def __init__(self, height, surface, color, price):
        self.height = height
        self.surface = surface
        self.color = color
        self.price = price
        self.volume = surface * height
        House.no_of_houses += 1 #cum functia __init__ este chemata la fiecare instanta a unei clase, variabila no_of_houses va fi incrementata mereu

    def print_location(self):
        print(House.location) #chiar si in interiorul clasei, variabilele se acceseaza tot prin intermediul clasei



house1 = House(10, 300, 'white', 100000)
house2 = House(15, 200, 'blue', 150000)
print(house1.volume)

house1.print_location()
print(House.location) # "variabila" location poate fi accesata doar prin intermediul clasei sau unei instante a clasei

house2.location = 'Pipera'

print(house1.location)
print(house2.location)
print(House.no_of_houses) # at each instantiating of the class 'House, this variabile is incremented.

House.print_location()
