from game import Board

method = Board()
i = 1
while i < 5:
    n_play = input("Enter the number of players")
    n_play = int(n_play)
    if n_play < 2 or n_play > 8:
        
        print("Please enter a number between 2 and 8")
        
    else:
        Board.start_game(method, n_play)
        i = 6

