import sys
from typing import List, Tuple, Dict

class Game:
    """
    Holds sets of games as arrays of red, green, and blue results
    """
    def __init__(self, id: int, moves_red: List[int], moves_green: List[int],
                 moves_blue: List[int]) -> None:
        """
        Create an instance of the Game object
        """
        self.game_id = id
        self.moves_red = moves_red
        self.moves_green = moves_green
        self.moves_blue = moves_blue
    
    def __str__(self) -> str:
        """
        toString()
        """
        return f"Red:   {*self.moves_red,}\nGreen: {*self.moves_green,}\nBlue:  {*self.moves_blue,}"

    def findMaxCubes(self) -> Tuple[int, int , int]:
        """
        Finds the maximum number for each color cube required for the set of
          games and returns the values as a tuple of Red, Green, Blue
        """
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
        """
        Returns `True` if the limit for each color cube is greater than or equal
          to the number of cubes required for a certain set of games
        """
        max_red, max_green, max_blue = self.findMaxCubes()
        return max_red <= red and max_green <= green and max_blue <= blue

    def power(self) -> int:
        """
        Calculates the "power" required for each set of games and returns an int
        """
        red_pow, green_pow, blue_pow = self.findMaxCubes()
        return red_pow * green_pow * blue_pow

games: Dict[int, Game] = {}

def parseInputs(fname: str):
    """
    Parses a list of games and creates objects for each set of games to be 
      stored in the `games` Dict.
    """
    with open(fname,"r") as f:
        # For each set of games
        for line in f:
            id: int = int(line.split(" ")[1][:-1])
            moveslist: List[str] = line.split(":")[1].split(";")
            red_moves: List[int] = []
            green_moves: List[int] = []
            blue_moves: List[int] = []
            num_moves: int = 0
            # For each game in the set
            for subgame in moveslist:
                moves: List[str] = subgame.split(",")
                num_moves += 1
                # For each color cube pulled
                for move in moves:
                    if "red" in move:
                        red_moves.append(int(move.split(" ")[1]))
                    elif "green" in move:
                        green_moves.append(int(move.split(" ")[1]))
                    elif "blue" in move:
                        blue_moves.append(int(move.split(" ")[1]))
                # If the red|green|blue cube wasn't listed we pulled zero
                if len(red_moves) < num_moves:
                    red_moves.append(0)
                if len(green_moves) < num_moves:
                    green_moves.append(0)
                if len(blue_moves) < num_moves:
                    blue_moves.append(0)
            # Newly parsed game goes in the dict
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
        # If the set can be played add the ID to the final count
        if game.canPlay(max_reds, max_green, max_blue):
            idValue += game.game_id
        powValue += game.power()
    print(idValue)
    print(powValue)