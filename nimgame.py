if __name__ == '__main__':
  print("Let's play Nim!")
  stones = 15
  players = ["P1","P2"]
  while True:
    print(f"{stones} stones left")
    for player in players:
      print(f"{player}'s turn!")
      
      while True:
        take = input("Take (1-3) stones? ")
        
        if take.isdigit():
          take = int(take)
        
        if take in [1,2,3]:
          stones -= take  
          print(f"{player} took {take} stones. {stones} left.")
          break
    if stones <= 0:
      print(f"{player} wins!")
    play_again = input("Play again (y/n)?")
    if play_again.lower() != 'y':
      print("Bye!")
      exit()
    
    stones = 15