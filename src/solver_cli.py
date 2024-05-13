import argparse
from card_game_solver import CardGameSolver  # Assuming the class is in a file named card_game_solver.py

def main():
    parser = argparse.ArgumentParser(description="CLI for solving the 24 Card Game")
    parser.add_argument("--solve", nargs=4, type=int, help="Solve the game for a hand of four numbers. Usage: --solve num1 num2 num3 num4")
    parser.add_argument("--list-hands", action="store_true", help="List all possible hands of four numbers.")
    parser.add_argument("--list-operations", action="store_true", help="List all possible operations combinations.")
    
    args = parser.parse_args()

    solver = CardGameSolver()

    if args.solve:
        hand = args.solve
        if len(hand) != 4:
            print("Please provide exactly four numbers.")
        else:
            solutions = solver.solve(hand)
            if solutions:
                print(f"Solutions for hand {hand}: {solutions}")
            else:
                print("No solutions found.")
    
    if args.list_hands:
        hands = solver.generate_hands()
        for hand in hands:
            print(hand)

    if args.list_operations:
        operations = solver.generate_operation_combinations()
        for operation in operations:
            print(operation)

if __name__ == "__main__":
    main()
