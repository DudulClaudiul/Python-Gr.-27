

class Observer:
    def update(self, msg):
        pass





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

    def notify(self, msg):
        for a in self.animals:
            a.update(msg)


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


class Dog(Animal, Observer):
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

    def update(self, msg):
        print(f"Dog with name: {self.name} has received your message: {msg} and is ignoring it!")


class Cat(Animal, Observer):
    def speak(self):
        print("meeow!!")

    def __str__(self):
        return f"Cat with name: {self.name}"

    def __repr__(self):
        return f"Cat('{self.name}')"

    def update(self, msg):
        print(f"Cat with name: {self.name} has received your message: {msg} and is happy to receive it!")


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
park.add_animal("The owner of the park has arrived and is asking all the animals to leave.")
park.notify("It started to rain in the park!")









