import random
def get_choices():
    player_choice = input("enter a choice(rock,paper,scissor):")
    opsions = ["rock","paper","scissor"]
    computer_choice = random.choice(opsions)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player,computer):
    print(f"You choose {player}, computer choose {computer}")
    if player == computer:
     return "its draw"
    elif player == "rock":
       if computer == "scissor":
          return "rock smashes scissor,You win"
       else:
         return "paper covers rock,You lose"
    
    elif player == "paper":
        if computer == "rock":
          return "paper covers rock,You win"
        else:
         return "sccisor cuts paper,You lose"
    
    elif player == "scissor":
       if computer == "paper":
          return "sccisor cut paper,You win"
       else:
        return "rock smash scissor,You lose" #return e kryn funksionin
    
choices = get_choices() 
result = check_win(choices["player"], choices["computer"])
print(result)