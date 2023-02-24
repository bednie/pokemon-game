import random

class Pokemon():
    
    def __init__(self, name: str, health: int=100, hit: int=20) -> None:
        self.name = name
        self.health = health
        self.hit_points = hit

    # Regular attack common to all pokemon
    def attack(self, Pokemon):
        if Pokemon.health > self.hit_points:
            Pokemon.health = Pokemon.health - self.hit_points
        else:
            Pokemon.health = 0
        print(f"{self.name} attacks!")
        print(f"{Pokemon.name} was hit!")
        
        self.print_health_status(Pokemon)


    def print_health_status(self,Pokemon):
        if Pokemon.health > 70:
            print(f"{Pokemon.name}'s Health: " + round(Pokemon.health/10)*"\U0001F7E9"
                + (10-round(Pokemon.health/10))*"\U00002B1C"
                + f" | {Pokemon.health}"
                + "\n-------------------------")
        elif Pokemon.health > 50:
            print(f"{Pokemon.name}'s Health: " + round(Pokemon.health/10)*"\U0001F7E8"
                + (10-round(Pokemon.health/10))*"\U00002B1C"
                + f" | {Pokemon.health}"
                + "\n-------------------------")
        elif Pokemon.health > 30:
            print(f"{Pokemon.name}'s Health: " + round(Pokemon.health/10)*"\U0001F7E7"
                + (10-round(Pokemon.health/10))*"\U00002B1C"
                + f" | {Pokemon.health}"
                + "\n-------------------------")
        elif Pokemon.health > 0:
            print(f"{Pokemon.name}'s Health: " + round(Pokemon.health/10)*"\U0001F7E5"
                + (10-round(Pokemon.health/10))*"\U00002B1C"
                + f" | {Pokemon.health}"
                + "\n-------------------------")
        else:
            print(f"{Pokemon.name} fainted!\n-------------------------")

    # Display basic information about this pokemon
    def say_hi(self):
        print(f"""\n\tName: {self.name}
\tHealth Points: {self.health}
\tHit Power: {self.hit_points}""")

    # Abstract method - Child class Pokemon implement special_attack
    def special_attack(self, Pokemon):
       print("Pokemon used its special attack!")
    

class GrassType(Pokemon):

    pokemon_type = "grass"
    weak_against = "fire"
    special_attack_name = "Solar Beam"


    def special_attack(self,opponent: Pokemon):
        print(f"{self.name} used {self.special_attack_name}.")
        if random.randint(1,10) > 3:
            print("It was a direct hit!")
            if self.pokemon_type == opponent.weak_against:
                print("It was super effective!")
                if opponent.health > self.hit_points:
                    opponent.health = opponent.health - (self.hit_points * 1.35)
                else:
                    opponent.health = 0
            else:
                if opponent.health > self.hit_points:
                    opponent.health = opponent.health - (self.hit_points * 1.15)
                else:
                    opponent.health = 0
            self.print_health_status(opponent)
        else:
            if random.choice([True,False]):
                print(f"{self.name} missed!" 
                    + "\n-------------------------")
            else:
                print(f"{opponent.name} defended itself!"
                    + "\n-------------------------") 


class WaterType(Pokemon):

    pokemon_type = "water"
    weak_against = "grass"
    special_attack_name = "Hydro Cannon"


    def special_attack(self, opponent: Pokemon):
        print(f"{self.name} used {self.special_attack_name}.")
        if random.randint(1,10) > 3:
            print("It was a direct hit!")
            if self.pokemon_type == opponent.weak_against:
                print("It was super effective!")
                if opponent.health > self.hit_points:
                    opponent.health = opponent.health - (self.hit_points * 1.35)
                else:
                    opponent.health = 0
            else:
                if opponent.health > self.hit_points:
                    opponent.health = opponent.health - (self.hit_points * 1.15)
                else:
                    opponent.health = 0
            self.print_health_status(opponent)
        else:
            if random.choice([True,False]):
                print(f"{self.name} missed!"
                    + "\n-------------------------")
            else:
                print(f"{opponent.name} defended itself!"
                    + "\n-------------------------")


class FireType(Pokemon):
    
    pokemon_type = "fire"
    weak_against = "water"
    special_attack_name = "Flamethrower"


    def special_attack(self,opponent: Pokemon):
        print(f"{self.name} used {self.special_attack_name}.")
        if random.randint(1,10) > 3:
            print("It was a direct hit!")
            if self.pokemon_type == opponent.weak_against:
                print("It was super effective!")
                if opponent.health > self.hit_points:
                    opponent.health = opponent.health - (self.hit_points * 1.35)
                else:
                    opponent.health = 0
            else:
                if opponent.health > self.hit_points:
                    opponent.health = opponent.health - (self.hit_points * 1.15)
                else:
                    opponent.health = 0
            self.print_health_status(opponent)
        else:
            if random.choice([True,False]):
                print(f"{self.name} missed!"
                    + "\n-------------------------")
            else:
                print(f"{opponent.name} defended itself!"
                    + "\n-------------------------")


    