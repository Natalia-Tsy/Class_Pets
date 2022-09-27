class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def perfect(self):
        return 'Pets are perfect'


class Cats(Pets):
    def __init__(self, name, age, breed, chip):
        super().__init__(name, age)
        self.breed = breed
        self.__chip = chip


    def cat(self):
        return 'There are no bad cats'

    def get_chip(self):
        return f'Chip number is {self.__chip}'


    def set_chip(self, new_chip):
        self.__chip = new_chip


class Dogs(Pets):
    def __init__(self, name, age, function):
        super().__init__(name, age)
        self.function = function


    def dog(self):
        return 'Dogs are best friends'


class Birds(Pets):
    def __init__(self, name, kind, colour):
        super().__init__(self, name)
        self.kind = kind
        self.colour = colour

    def bird(self):
        return 'Best singers ever'

cat1 = Cats('Phoenix', '3', 'metis', '152')
print(cat1.name)
cat1.chip = '765'
print(cat1.chip) #765
print(cat1.get_chip()) #Chip number is 152
print(cat1.perfect())
print(cat1.cat())
dog1 = Dogs('Rex', '6', 'hunter')
print(dog1.function)
print(dog1.dog())
bird1 = Birds('Tima', 'budgie', 'blue')
print(bird1.colour)
print(bird1.bird())
print(cat1.get_chip()) # Chip number is 152
cat1.__chip = '541'
print(cat1.__chip) #541
print(cat1.chip) #765




