"""
Course: Introduction to Python Programming
Student Name: Arturo Filio Villa
"""
# 
from random import randint
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# 
def HumanPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''
    valid = False
    while valid == False:
      p_choice = input(
        "rock(r), paper(p), scissors(s)? \
        \nor you want to see the a record of the game (g)? \
        \nor you want o quit(q)?\n"
      )

      if (p_choice == 'r' or p_choice == 'p' or p_choice == 's' 
        or p_choice == 'q' or p_choice == 'g'):
        valid = True
        return p_choice
      else:
        print("\nThat is not a valid choice please select the following:\n")
# 
def ComputerPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''
    c_choice = randint(1,3)
    if c_choice == 1:
      c_choice = 'r'
    if c_choice == 2:
      c_choice = 'p'
    if c_choice == 3:
      c_choice = 's'
    
    return c_choice

#
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''
    # Check first if the ChoiceofHuman is not g or q
    if ChoiceOfHumanPlayer == 'g' or ChoiceOfHumanPlayer == 'q':
      return

    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
      return 0

    if ChoiceOfComputerPlayer != ChoiceOfHumanPlayer:  
      
      if ChoiceOfComputerPlayer == 's':
        if ChoiceOfHumanPlayer == 'r':
          return 2
        else:
          return 1
      
      if ChoiceOfComputerPlayer == 'r':
        if ChoiceOfHumanPlayer == 's':
          return 1
        else: 
          return 2

      if ChoiceOfComputerPlayer == 'p':
        if ChoiceOfHumanPlayer == 's':
          return 2
        else: 
          return 1

# 
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''
    won = ""
    if Outcome == 0:
      won = "\n---------It's a tie!---------\n"
    if Outcome == 1:
      won = "\n---------The computer won!---------\n"
    if Outcome == 2:
      won = "\n---------You won!---------\n"

    print(won, "Computer chose:", ChoiceOfComputerPlayer, "You chose:", ChoiceOfHumanPlayer, "\n\n")
# 
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
    # Check that the player didn't quit the game or asked for info, that way you don't append the 'g' or the 'q'
    if ChoiceOfHumanPlayer == 'q' or ChoiceOfHumanPlayer == 'g':
      return
    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)
# 
def PrintGameRecord(GameRecord):
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
    player_wins = 0
    computer_wins = 0
    draws = 0
    for win in GameRecord[2]:
      if win == 2 and len(GameRecord) > 1:
        player_wins += 1
      if win == 0:
        draws += 1
      if win == 1:
        computer_wins += 1

    num_rounds = len(GameRecord[2])
    print("\nThe number of rounds played is:", num_rounds, " , you've won:", player_wins, " rounds, computer has won: ", computer_wins, "rounds and",
          " there has been:", draws, "daws" )

# the game
def PlayGame():
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''
    game = True
    players_choices = []
    computers_choices = []
    outcomes = []
    GameRecord = [players_choices, computers_choices, outcomes]

    while game == True:
      print("-----------------NEW ROUND-----------------")
      print("\nWelcome to rock-paper-scissors !\n")
      
      human_outcome = HumanPlayer(GameRecord)
      computer_outcome = ComputerPlayer(GameRecord)
      outcome = Judge(computer_outcome, human_outcome)
      
      PrintOutcome(outcome, computer_outcome, human_outcome)
      
      if human_outcome == 'g':
        PrintGameRecord(GameRecord)
      
      if human_outcome == 'q':
        print("You quitted the game")
        game = False
        return
      
      UpdateGameRecord(GameRecord, computer_outcome, human_outcome, outcome)
      
    
# do not modify anything below
if __name__ == '__main__':
    PlayGame()
