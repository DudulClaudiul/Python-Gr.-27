

class AnimalPark:
    def __init__(self):
        self.animals = []

    def add_animal(self, anim):
        # punem o conditie aici, lasam doar animale in park!
        # isinstance verifica daca anim este o instanta a unei clase care este ori Animal ori mosteneste Animal, ori mosteneste orice alta clasa care mosteneste Animal.
        if isinstance(anim, Animal):
            self.animals.append(anim)

    def make_noise(self):
        for a in self.animals:
            # polymorphism
            a.speak()


class Animal:
    def __init__(self, name="Generic", age=1):
        self.name = name
        self.age = age

    def speak(self):
        print("Animal goes poof!")

    def __str__(self):
        return f"Animal with name: {self.name}"

    def __repr__(self):
        return f"Animal('{self.name}')"


class Dog(Animal):
    def __init__(self, name, age=1, breed="Corcitura"):
        # apelam constructorul parintelui
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("Woof!")

    def lick(self):
        print("Dog licks you!")

    def __str__(self):
        return f"Dog with name: {self.name}"

    def __repr__(self):
        return f"Dog('{self.name}')"

class Cat(Animal):
    def speak(self):
        print("meeow!!")

    def __str__(self):
        return f"Cat with name: {self.name}"

    def __repr__(self):
        return f"Cat('{self.name}')"


class Bat(Dog):
    def __str__(self):
        return f"Bat with name: {self.name}"

    def __repr__(self):
        return f"Bat('{self.name}')"


anim1 = Animal()
print("Animal.speak()")
anim1.speak()

dog1 = Dog("Spot")
cat1 = Cat("Shadow")

print("Dog.speak()")
dog1.speak()
print("Cat.speak()")
cat1.speak()
dog1.lick()

print(dog1.name)
print(cat1.name)

print("=======Animal Park=========")

cat2 = Cat("Paw")
bat1 = Bat("Man Bat")
park = AnimalPark()
park.add_animal(dog1)
park.add_animal(cat1)
park.add_animal(cat2)
park.add_animal(bat1)
print(park.animals)
park.make_noise()










