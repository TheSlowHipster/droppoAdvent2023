import sys
from typing import List, Tuple, Dict

class Game:
    game_id: int
    moves_red: List[int]
    moves_green: List[int]
    moves_blue: List[int]

    def __init__(self, id: int, moves_red: List[int], moves_green: List[int],
                 moves_blue: List[int]) -> None:
        self.game_id = id
        self.moves_red = moves_red
        self.moves_green = moves_green
        self.moves_blue = moves_blue
    
    def __str__(self) -> str:
        return f"Red:   {*self.moves_red,}\nGreen: {*self.moves_green,}\nBlue:  {*self.moves_blue,}"

    def findMaxCubes(self) -> Tuple[int, int , int]:
        max_red = 0
        max_green = 0
        max_blue = 0
        for game in self.moves_red:
            if game > max_red:
                max_red = game
        for game in self.moves_green:
            if game > max_green:
                max_green = game
        for game in self.moves_blue:
            if game > max_blue:
                max_blue = game
        return max_red, max_green, max_blue
    
    def canPlay(self, red: int, green: int, blue: int) -> bool:
        max_red, max_green, max_blue = self.findMaxCubes()
        return max_red <= red and max_green <= green and max_blue <= blue

    def power(self):
        red_pow, green_pow, blue_pow = self.findMaxCubes()
        return red_pow * green_pow * blue_pow

games: Dict[int, Game] = {}

def parseInputs(fname: str):
    with open(fname,"r") as f:
        for line in f:
            id: int = int(line.split(" ")[1][:-1])
            moveslist: List[str] = line.split(":")[1].split(";")
            red_moves: List[int] = []
            green_moves: List[int] = []
            blue_moves: List[int] = []
            num_moves: int = 0
            for subgame in moveslist:
                moves: List[str] = subgame.split(",")
                num_moves += 1
                for move in moves:
                    if "red" in move:
                        red_moves.append(int(move.split(" ")[1]))
                    elif "green" in move:
                        green_moves.append(int(move.split(" ")[1]))
                    elif "blue" in move:
                        blue_moves.append(int(move.split(" ")[1]))
                if len(red_moves) < num_moves:
                    red_moves.append(0)
                if len(green_moves) < num_moves:
                    green_moves.append(0)
                if len(blue_moves) < num_moves:
                    blue_moves.append(0)
                
            games[id] = Game(id, red_moves, green_moves, blue_moves)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        fname = "smallTest2.txt"
    else:
        fname = sys.argv[1]
    max_reds = 12
    max_green = 13
    max_blue = 14
    parseInputs(fname)
    idValue = 0
    powValue = 0
    for game in games.values():
        if game.canPlay(max_reds, max_green, max_blue):
            idValue += game.game_id
        powValue += game.power()
    print(idValue)
    print(powValue)