import pokemon
import random

class Turn():
    def __init__(self, player: pokemon.Pokemon, opponent: pokemon.Pokemon) -> None:
        if random.choice([True, False]):
            self.current_turn = player
            self.next_turn = opponent
        else: 
            self.current_turn = opponent
            self.next_turn = player
        
    
    def turn(self):
        this_move = self.current_turn
        self.current_turn = self.next_turn
        self.next_turn = this_move
        return this_move