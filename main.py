import pokemon
import turn_handler
import time
import random
import player_choose_attack

def main():

    # Get player choice of pokemon
    player_type_choice = ""
    print("Enter your pokemon type:\n"
        + "\t'F' - Fire Type: Charmander\n"
        + "\t'G' - Grass Type: Bulbasaur\n"
        + "\t'W' - Water Type: Squirtle\n")

    while True:
        try:
            player_type_choice = str(input().upper())
        except ValueError:
            print("\nInvalid selection! Try again.\nPlease enter 'F', 'G', or 'W'.")
            continue
    
        if player_type_choice not in ['F','G','W']:
            print("\nInvalid selection! Try again.\nPlease enter 'F', 'G', or 'W'.")
            continue

        else:
            
            # Get player's name for pokemon
            while True:
                try:
                    print("Enter your pokemon's name: ")
                    player_name = str(input())
                except ValueError:
                    print("\nTry again.\nPlease enter a valid name.")
                else:
                    if player_type_choice == 'G':
                        player_pokemon = pokemon.GrassType(player_name, 100, 20)
                    elif player_type_choice == 'F':
                        player_pokemon = pokemon.FireType(player_name, 100, 20)
                    elif player_type_choice == 'W':
                        player_pokemon = pokemon.WaterType(player_name, 100, 20)
                    break
            break

    # Randomly select a pokemon type for the computer opponent
    computer_type = random.choice(["WaterType","FireType","GrassType"])
    if computer_type == "WaterType":
        computer_pokemon = pokemon.WaterType("Squirtle", 100, 20)
    elif computer_type == "GrassType":
        computer_pokemon = pokemon.GrassType("Bulbasaur", 100, 20)
    elif computer_type == "FireType":
        computer_pokemon = pokemon.FireType("Charmander", 100, 20)

    
    player_pokemon.say_hi()
    print("\n\t----- vs -----")
    computer_pokemon.say_hi()
    print("\n")

    turn = turn_handler.Turn(player_pokemon,computer_pokemon)

    while True: # player_pokemon.health > 0 and computer_pokemon.health > 0:

        this_move = turn.turn() # decide whose move it is this turn

        if this_move is player_pokemon:

            # get player choice of move
            player_attack_choice = player_choose_attack.attack_choice()
            if player_attack_choice == 'S':
                player_pokemon.special_attack(computer_pokemon)
            elif player_attack_choice == 'R':
                player_pokemon.attack(computer_pokemon)

            if computer_pokemon.health <= 0:
                print(f"Game over. {player_pokemon.name} won!"
                    + "\n-------------------------\n")
                break

        elif this_move is computer_pokemon:
            if random.choice([True,False]):
                computer_pokemon.attack(player_pokemon)
            else:
                computer_pokemon.special_attack(player_pokemon) 
            if player_pokemon.health <= 0:
                print(f"Game over. {computer_pokemon.name} won!"
                    + "\n-------------------------\n")
                break
        
        time.sleep(2)
        
if __name__ == "__main__":
    main()