class Animal:


    def __init__(self, name, appetite, is_hungry: bool = True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry


    def print_name(self):
        print(f"Hello, I'm {self.name}")


    def feed(self):
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
        self.is_hungry = False
        return self.appetite
        # se não estiver com fome: retorna 0
        return 0


class Cat(Animal):


    def catch_mouse(self):
        print(f"The hunt began!")


class Dog(Animal):


    def __init__(self, name, is_hungry: bool = True):
        super().__init__(name, 7, is_hungry)


    def bring_slippers(self):
        print(f"The slippers delivered!")


def feed_animals(animais: list):
    return sum(animal.feed() for animal in animais)
