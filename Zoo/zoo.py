class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"This animal's is {self.name}, and age is {self.age}, health level is {self.health}, happiness level is {self.happiness}")

    def feed(self):
        self.health += 15
        self.happiness += 15
        return self

class Lion(Animal):
    def __init__(self, name, age, health=100, happiness=100):
        super().__init__(name, age, health, happiness)

    def feed(self):
        self.health += 20
        self.happiness += 20
        print("I have eat my launch!")
        return self


class Penguin(Animal):
    def __init__(self, name, age, health=100, happiness=100):
        super().__init__(name, age, health, happiness)

    def feed(self):
        self.health += 30
        self.happiness += 30
        print("I ate so much")
        return self 



class Monkey(Animal):
    def __init__(self, name, age, health=100, happiness=100):
        super().__init__(name, age, health, happiness)

    def feed(self):
        self.health += 40
        self.happiness += 40
        print("I have eaten today")
        return self


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age):
        self.animals.append(Lion(name, age))
        return self
    
    def add_penguin(self, name, age):
        self.animals.append(Penguin(name, age))
        return self
    
    def add_monkey(self, name, age):
        self.animals.append(Monkey(name, age))
        return self
            
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

    def feed(self, animal):
        self.animals[animal].feed()
        return self


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 30)
zoo1.add_lion("Simba", 50).add_penguin("Rajah", 60).add_monkey("Shere Khan", 10).feed(0).feed(1).feed(2).feed(3).print_all_info()
