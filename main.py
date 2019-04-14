from kuromasu import Kuromasu
from boards import BOARDS

for boardType in BOARDS:
    for board in boardType:
        game = Kuromasu(board)
        print("\nFor a depth-first algorithm: ")
        game.solve("DF")
        game.print()

        print("\nFor a A* algorithm: ")
        game.solve("Astar")
        game.print()
        print(50*"-")
