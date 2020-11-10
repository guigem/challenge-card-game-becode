from game import Board

#called the method start_game
method = Board()
i = 1

#making sure the user inserts between 2 and 8 players
while i < 5:
    n_play = input("Enter the number of players")
    n_play = int(n_play)
    if n_play < 2 or n_play > 8:
        
        print("Please enter a number between 2 and 8")
        
    else:
        
        # start the game and leave the while loop when it is over
        Board.start_game(method, n_play)
        i = 7

