from kuromasu import Kuromasu
from boards import BOARDS

for boardType in BOARDS:
    for board in boardType:
        game = Kuromasu(board)
        print("For a depth-first algorithm: \n")
        game.solve("DF")
        game.print()

        print("For a A* algorithm: \n")
        game.solve("Astar")
        game.print()
