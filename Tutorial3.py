

class City:

    classification = 'urban'
    tallest_building = 828                          # stim ca cea mai inalta cladire are 828 de metri
    def __init__(self, population, surface, country):
        self.population = population
        self.surface = surface
        self.country = country

    def density_calculator(self):
        return self.population/self.surface

    @classmethod                                #explic @classmethod mai jos
    def change_tallest_building(cls, height):
        cls.tallest_building = height


Bucharest = City(2000000, 240, 'Romania')
Paris = City(2800000, 105, 'France')

print(Bucharest.density_calculator())

City.change_tallest_building(1000)
print (City.tallest_building)
print(Paris.tallest_building)



"""

 O metoda 'obisnuita', numita corect instance method (def func (self), poate accesa doar instantele unei clase. Spre exemplu, daca incerc:

City.density_calculator()

voi primi o eroare, pentru ca metoda functioneaza doar pe o INSTANTA a clasei (este si logic, avand parametrul self).

Class methods, create aplicand decoratorul @classmethod asupra unei metode, sunt metode ce preiau clasa, in loc de instanta unei clase, ca parametru.
De exemplu, in cazul nostru, prin class method-ul 'change_tallest_building' pot schimba valoarea variabilei tallest_building la nivel de CLASA. Practic,

City.change_tallest_building(1000) este echivalent cu City.tallest_building = 1000

"""
