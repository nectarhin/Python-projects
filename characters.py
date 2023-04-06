class Character():
    def __init__(self,name,health,mana):
        self.name = name
        self.health = health
        self.mana = mana

    def description_character(self):
        description = self.name + ' has ' + str(self.health) + ' hp ' + str(self.mana) + ' mana'
        print(description)


class warrior (Character):
    def __init__(self,name,health,mana):
        super().__init__(name,health,mana)
        self.charge = 100
        self.rage = 100

    def get_rage(self):
        print('rage is ' + str(self.rage))
    def get_charge(self):
        print('charge is ' + str(self.charge))

class mage (Character):
    def __init__(self,name,health,mana):
        super().__init__(name,health,mana)
        self.fireball = 100
        self.ice_spike = 100

    def get_fireball(self):
        if self.fireball == 100:
            print('fireball is ready')
        else:
            print('not ready yet')
    def get_ice_spike(self):
        if self.ice_spike == 100:
            print('ice spike is ready')
        else:
            print('not ready yet')


class archer(Character):
    def __init__(self,name,health,mana):
        super().__init__(name,health,mana)
        self.trippleshot = 100
        self.penetration = 100

    def get_trippleshot(self):
        if self.trippleshot == 100:
            print('trippleshot is ready')
        else:
            print('not ready yet')
    def get_penetration(self):
        if self.penetration == 100:
            print('penetration is ready')
        else:
            print('not ready yet')

warrior = warrior('Warrior',320,80)
mage = mage('Mage',160,350)
archer = archer('Archer',210,150)


warrior.description_character()
warrior.get_charge()
warrior.get_rage()
print('\n')



mage.description_character()
mage.get_fireball()
mage.get_ice_spike()
print('\n')


archer.description_character()
archer.get_trippleshot()
archer.get_penetration()
print('\n')


