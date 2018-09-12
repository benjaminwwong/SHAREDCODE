"""#Go fish
n = int(input("How many anglers are on the prowl today?:"))

deck = []

values = [1,2,3,4,5,6,7,8,9,10, "J", "Q", "K"]

suits = ["S", "D", "C", "H"]

for v in values:
    for s in suits:
        deck.append(str(v) + s)

print(deck)"""
    
class Battle:
    def __init__(self, heroes, enemies):
        self.heroes = heroes
        self.enemies = enemies

    def __repr__(self):
        return("combat between %s and %s" %(self.heroes, self.enemies))
class Hero:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp
    def __repr__(self):
        return self.name

class Evil:
    def __init__(self, name, atk ,hp):
        self.name = name
        self.atk = atk
        self.hp = hp
    def __repr__(self):
        return self.name

soph = Hero("SophiaJ", 13, 25)

ben = Hero("BenJay", 12, 25)

bart = Hero("BrotherBART",9 , 30)

jlaird = Hero("Jlaird", 20, 13)

dragon = Evil("Dragon", 5, 40)

wyrm = Evil("Wyrm", 6, 40)

wyvern = Evil("wyvern", 10, 50)

h1 = [soph, ben, bart, jlaird]


e1 = [dragon, wyrm, wyvern]

for ind, n in enumerate(h1):
    print(n)
    print(e1[ind])

