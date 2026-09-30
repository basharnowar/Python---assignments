class Backpack:
    def __init__(self, owner, coins=0):
        self.owner =  owner
        self.coins = coins

    def add_coins(self, amount):
        self.coins += amount
        return self

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
        else:
            print("Not enough coins")
        return self

    def display(self):
        print(f"{self.owner}'s backpack has {self.coins} coins")
        return self

class Hero:
    def __init__(self, name):
        self.name = name
        self.backpack = Backpack(name)


    def collect(self, amount):
        self.backpack.add_coins(amount)  # <- this one was self.backpack.add_coins += amount which is wrong, add_coins is a method not an attribute thath holds a number.
        return self


    def buy_item(self, amount):
        self.backpack.spend_coins(amount)
        return self


    def gift_coins(self, other_hero, amount):
        if self.backpack.coins >= amount:
            self.backpack.spend_coins(amount)
            other_hero.backpack.add_coins(amount)
        return self




hero1 = Hero("Lina")
hero2 = Hero("Omar")

hero1.collect(50).buy_item(15).gift_coins(hero2, 20)


hero1.backpack.display()
hero2.backpack.display()



# After using the RCFT, the Ai was better in explaining in fact, he spotted 4 problems
# and was better at explaining instead of throughing him the code and just fix
# because when I used the weak prompt, he spotted only 2 problems gave me the solution without explaining!