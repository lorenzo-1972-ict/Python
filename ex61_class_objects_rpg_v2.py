class Hero:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.attack = 10
        self.inventory = {}
        self.ability = {}
        print("\nHero: ", self.name," / ", self.hp,"hp / ", self.attack,"attack(s)")

    def fight(self, monster):
        monster_new_hp = monster.get_hp() - self.attack
        monster.set_hp(monster_new_hp)

    def get_hp(self):
        return self.hp
    
    def set_hp(self, new_hp):
        self.hp = new_hp

    def xp_gain(self):
        self.hp += 10

    def object_add(self, object_type, quantity):
        if object_type in self.inventory:
            self.inventory[object_type] += quantity
        else:
            self.inventory[object_type] = quantity

    def object_use(self, object_type):
        if object_type == "potion" and self.inventory[object_type] !=0:
            self.hp += 5
            self.inventory[object_type] -= 1

    def ability_add(self, ability_type, ability_damage):
        if ability_type not in self.ability:
            self.ability[ability_type] = ability_damage
        else:
            print("Hero already possess this ability.")

    def ability_use(self, ability_type, opponent):
        if ability_type in self.ability:
            opponent.hp -= self.ability[ability_type]
            self.hp -= 10

class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = 60
        self.attack = 5
        print("\nMonster", self.name," / ", self.hp,"hp / ", self.attack,"attack(s)")

    def fight(self, hero):
        hero_new_hp = hero.get_hp() - self.attack
        hero.set_hp(hero_new_hp)
        
    def get_hp(self):
        return self.hp
    
    def set_hp(self, new_hp):
        self.hp = new_hp        


def ongoing_fight(hero, monster):

    while (hero.get_hp() > 0 and monster.get_hp() > 0):
        print("\nHero remaining hp: ", hero.get_hp())
        print("\nMonster remaining hp: ", monster.get_hp())
        hero.fight(monster)
        monster.fight(hero)

    print("\nHero remaining hp: ", hero.get_hp())
    print("\nMonster remaining hp: ", monster.get_hp())    

    if (hero.get_hp() <= 0):
        print("\nFight winner: ", monster.name)
    else:
        print("\nFight winner: ", hero.name)
        hero.xp_gain()
        print("\nHero new hp: ", hero.hp)

def main():
    hero1 = Hero("Aragorn")
    monster1 = Monster("Goblin")
    # ongoing_fight(hero1, monster1)
    hero1.ability_add("Crush attack", 40)
    print(hero1.ability)
    hero1.ability_use("Crush attack", monster1)
    print(monster1.hp)
    print(hero1.hp)

main()