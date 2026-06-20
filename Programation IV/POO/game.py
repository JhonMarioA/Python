
class Character():     #parent class
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!" )

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        print(f"{self.name} takes {amount} damage! Remaining health: {self.health}")

    def is_alive(self):
        return self.health > 0


class Player(Character): #inheriting from the parent class
    def __init__(self, name, health, attack_power, defense, inventory, experience, level):
        super().__init__(name, health, attack_power, defense)
        self.inventory = inventory
        self.experience = experience
        self.level = level


class Enemy(Character):  #inheriting from the parent class

    def __init__(self, name, health, attack_power, defense, type_, reward):
        super().__init__(name, health, attack_power, defense)
        self.type = type_
        self.reward = reward
    
    def special_attack(self, target):
        damage = max(0, (self.attack_power * 2) - target.defense)
        target.take_damage(damage)
        print(f"{self.name} uses a special attack on {target.name} for {damage} damage!")


class Item():
    def __init__(self, name, type_, value):
        self.name = name
        self.type = type_
        self.value = value

    def use(self, target):
        if self.type == "heal":
            target.health += self.value
            print(f"{target.name} heals {self.value} points! New health: {target.health}") 
        elif self.type == "boost_attack":
            target.attack_power += self.value
            print(f"{self.name}'s attack increases by {self.value}!")


class Battle():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def start(self):
        print(f"A wild {self.enemy.name} appears!")
        while self.player.is_alive() and self.enemy.is_alive():
            action = input("Do you want to (a)ttack or (i)tem?").lower()
            
            if action == "a":
                self.player.attack(self.enemy)

            elif action == "i" and self.player.inventory:
                item = self.player.inventory.pop()
                item.use(self.player)

            else:
                print("Invalid choice.")

            if self.enemy.is_alive():
                self.enemy.attack(self.player)
        print("Battle over!")

class Game(): #...
    pass


player = Player("Hero", 50, 10, 3, [Item("Potion", "heal", 20)], 0, 1)
enemy = Enemy("Goblin", 30, 8, 2, "basic", 10)

battle = Battle(player, enemy)
battle.start()






