

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If both players choose the same option, the game is a tie

import argparse

parser = argparse.ArgumentParser("Play rock, scissors, paper game")
parser.add_argument('Player_1', type=str, help="Choose one of rock, scissors, paper")
parser.add_argument('Player_2', type=str, help="Choose one of rock, scissors, paper")
args = parser.parse_args()

possible_values = ["rock", "paper", "scissors"]

value_map = {
    ("rock", "scissors"): [1, "Rock crushes scissors"],
    ("rock", "paper"): [2, "Paper covers rock"],
    ("paper", "scissors"): [2, "Scissors cuts paper"],
    ("paper", "rock"): [1, "Paper covers rock"],
    ("scissors", "rock"): [2, "Rock crushes scissors"],
    ("scissors", "paper"): [1, "Scissors cuts paper"],
    }

# if args.Player_1 not in possible_values or args.Player_2 not in possible_values:
#     print("invalid")
# elif args.Player_1 == args.Player_2:
#     print("It's a tie")
# else:
#     print(f"Player 1 played {args.Player_1}")
#     print(f"Player 2 played {args.Player_2}\n")
#     print(f"{value_map.get((args.Player_1, args.Player_2))[1]}\n")
#     print(f"Player {value_map.get((args.Player_1, args.Player_2))[0]} wins")

if args.Player_1 is None or args.Player_2 is None:
    print("Please choose")
    