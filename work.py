# Creating Pokemon class
class Pokemon:

    # Initialization
    def __init__(self, name, level, type, base_damage, max_health):
        self.name = name
        self.level = level
        type = type.lower()
        if type == "fire":
            self.type = 0
        elif type == "water":
            self.type = 1
        elif type == "grass":
            self.type = 2
        else:
            self.type = 3
        self.health = max_health
        self.base_damage = base_damage
        self.max_health = max_health
        self.is_knocked_out = False
        for i in range(2, level):
            self.max_health += 25
            self.base_damage += 10
        self.health = self.max_health
        self.owned = 0

        print(self.name + " now has " + str(self.max_health) + " HP")

    # Knock Down Pokemon
    def knock_out(self):
        if self.health <= 0:
            self.is_knocked_out = True
            print(self.name + " has been knocked out")

    # Damage Pokemon
    def lose_health(self, health):
        if self.health <= health:
            if not self.is_knocked_out:
                print(self.name + " has lost " + str(self.health) + " HP")
                self.health = 0
                self.knock_out()
            else:
                print(self.name + " is already knocked out")
        else:
            if not self.is_knocked_out:
                self.health -= health
                print(self.name + " has lost " + str(health) + " HP")
                print(self.name + " now has " + str(self.health) + " HP")
            else:
                print(self.name + "is already knocked out")

    # Heal Pokemon
    def gain_health(self, health):
        if self.health + health <= self.max_health:
            if not self.is_knocked_out:
                self.health += health
                print(self.name + " has gained " + str(health) + " HP")
                print(self.name + " now has " + str(self.health) + " HP")
            else:
                print(self.name + " is knocked out, revive him first")
        elif self.health == self.max_health:
            if not self.is_knocked_out:
                print(self.name + " is at max HP")
            else:
                print(self.name + " is knocked out, revive him first")
        elif self.health + health >= self.max_health:
            if not self.is_knocked_out:
                print(self.name + " has gained " + str(self.max_health - self.health) + " HP")
                self.health = self.max_health
                print(self.name + " now has " + str(self.health) + " HP")
            else:
                print(self.name + " is knocked out, revive him first")

    # Revive Pokemon
    def pokemon_revive(self):
        if not self.is_knocked_out:
            print(self.name + " is already alive")
        else:
            self.health = self.max_health
            self.is_knocked_out = False
            print(self.name + " has been revived")
            print(self.name + " now has " + str(self.health) + " HP")

    # Attack Another Pokemon
    def pokemon_attack(self, pokemon):
        if not self.is_knocked_out and not pokemon.is_knocked_out:
            print(self.name + " has attacked " + pokemon.name)
            if self.type == 0 and pokemon.type == 2:
                print("Bonus damage gained")
                pokemon.lose_health(2 * self.base_damage)
            elif self.type == 1 and pokemon.type == 0:
                print("Bonus damage gained")
                pokemon.lose_health(2 * self.base_damage)
            else:
                pokemon.lose_health(self.base_damage)
        elif self.is_knocked_out:
            print(self.name + " is knocked out")
        elif pokemon.is_knocked_out:
            print(pokemon.name + " is already knocked out")


# Creating Trainer Class
class Trainer:

    # Initialization
    def __init__(self, name, potions, revive_potions):
        self.pokemon_set = []
        self.name = name
        self.potions = potions
        self.active_pokemon = None
        self.revive_potions = revive_potions

    # Add Pokemon to trainer's set
    def add_pokemon(self, pokemon):
        if len(self.pokemon_set) <= 2 and pokemon not in self.pokemon_set and pokemon.owned == 0:
            self.pokemon_set.append(pokemon)
            pokemon.owned = 1
        elif len(self.pokemon_set) <= 2 and pokemon in self.pokemon_set:
            print("{} already has {}".format(self.name, pokemon.name))
        elif not len(self.pokemon_set) <= 2:
            print(self.name + " has max number of Pokemons")
        elif pokemon.owned != 0:
            print(pokemon.name + " is owned by another trainer")

    # Heals Pokemon
    def heal_pokemon(self):
        if self.active_pokemon is not None:
            if self.potions >= 1 and self.active_pokemon.health != self.active_pokemon.max_health:
                print("{} has healed his Pokemon".format(self.name))
                self.active_pokemon.gain_health(100)
                self.potions -= 1
            elif self.potions != 0 and not self.active_pokemon.health != self.active_pokemon.max_health:
                self.active_pokemon.gain_health(100)
            else:
                print(self.name + " has no more healing potions")
        else:
            print(self.name + " has no active pokemon")

    # Shows Pokemons
    def show_pokemons(self):
        if len(self.pokemon_set) == 1:
            print("{} currently has {}".format(self.name, self.pokemon_set[0].name))
        elif len(self.pokemon_set) == 2:
            print("{} currently has {} and {}".format(self.name, self.pokemon_set[0].name, self.pokemon_set[1].name))
        elif len(self.pokemon_set) == 3:
            print("{} currently has {}, {} and {}".format(self.name, self.pokemon_set[0].name, self.pokemon_set[1].name,
                                                          self.pokemon_set[2].name))
        else:
            print("{} currently has no pokemons".format(self.name))

    # Sets the active pokemon
    def set_active_pokemon(self, pokemon):
        if pokemon in self.pokemon_set:
            self.active_pokemon = pokemon
            print(self.name + " has set " + self.active_pokemon.name + " as an active pokemon")
        else:
            print(self.name + " doesn't have this pokemon")

    # Attacks another trainer's pokemon
    def attack(self, trainer):
        if self.active_pokemon is not None and trainer.active_pokemon is not None:
            print(self.name + " is attempting to attack " + trainer.name)
            self.active_pokemon.pokemon_attack(trainer.active_pokemon)
        elif self.active_pokemon is None:
            print(self.name + " has no active Pokemon")
        elif trainer.active_pokemon is None:
            print(trainer.name + " has no active Pokemon")

    # Revive a knocked out pokemon
    def revive_pokemon(self):
        if self.revive_potions >= 1:
            if self.active_pokemon is not None:
                print(self.name + " is attempting to revive " + self.active_pokemon.name)
                self.active_pokemon.pokemon_revive()
                self.revive_potions -= 1
            else:
                print(self.name + " is attempting to revive " + self.active_pokemon.name)
                print(self.name + " has no active pokemon")
        else:
            print(self.name + " has no revive potions")


# Creating Pokemon Object
charmander = Pokemon("Charmander", 12, "Fire", 20, 108)
bulbasaur = Pokemon("Bulbasaur", 13, "Grass", 25, 110)
wartortle = Pokemon("Wartortle", 14, "Water", 19, 115)
pikachu = Pokemon("Pikachu", 17, "Electric", 21, 112)
mewtwo = Pokemon("Mewtwo", 15, "Psychic", 18, 109)
suicune = Pokemon("Suicune", 16, "Suicune", 20, 114)

# Creating Trainer Objects
ethan = Trainer("Ethan", 2, 3)
nate = Trainer("Nate", 2, 2)

############################ PROJECT DONE ############################
# Deigned completely by Mohamed Emad

