class Class:
    def __init__(self, name, description, spells, max_stats):
        self.name = name
        self.description = description
        self.spells = spells
        self.max_stats = max_stats

    def __repr__(self):
        return self.name


classes = ["Swordsman", "Sage", "Luminary", "Priest", "Thief", "Magic Knight"]

weapons = ["Sword", "Staff", "Bow", "Axe", "Spear", "Gauntlets"]

swordsman = Class("Swordsman", "Front line fighters who choose to dedicate themselves to the blade. They wield Swords and Axes.", None, {"HP":600, "MP":180, "DEF":576 , "RES":480 , "ATK":475  , "MAG": 100, "LUK":384 , "SKL":470})

print(swordsman)
