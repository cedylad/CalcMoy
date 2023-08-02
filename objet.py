class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenu", pseudo, " / Vie :", health, "/ Attaque :", attack)

    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
    def attack_player(self, target_player):
        target_player.damage(self.attack)


class Warrior(Player):
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("Bienvenu warrior", pseudo, " / Vie :", health, "/ Attaque :", attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Armor +3")

    def get_armor_point(self):
        return self.armor




player = Player("Cedy", 20, 2)
player.damage(3)

warrior = Warrior("Ydec", 30, 4)
warrior.damage(4)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_point())

if issubclass(Warrior, Player):
    print("Guerrier est bien player")