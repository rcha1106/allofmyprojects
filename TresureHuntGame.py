import random


def treasure_hunt():
    size = 5
    max_turns = 12

    player_row = 0
    player_column = 0

    treasure_row = random.randint(0, size - 1)
    treasure_column = random.randint(0, size - 1)

    while treasure_row == 0 and treasure_column == 0:
        treasure_row = random.randint(0, size - 1)
        treasure_column = random.randint(0, size - 1)

    print("Welcome to the Treasure Hunt!")
    print("Find the treasure before you run out of turns.")
    print("Move with W, A, S, and D.")

    turn = 0

    while turn < max_turns:
        print(f"\nTurn {turn + 1} of {max_turns}")
        print(f"You are at row {player_row + 1}, column {player_column + 1}")

        distance = abs(player_row - treasure_row) + abs(
            player_column - treasure_column
        )

        if distance <= 1:
            print("You feel the treasure is very close!")
        elif distance <= 3:
            print("You are getting warmer.")
        else:
            print("The treasure is far away.")

        move = input("Choose a direction (W/A/S/D): ").lower()

        new_row = player_row
        new_column = player_column

        if move == "w":
            new_row -= 1
        elif move == "s":
            new_row += 1
        elif move == "a":
            new_column -= 1
        elif move == "d":
            new_column += 1
        else:
            print("Invalid move. Use W, A, S, or D.")
            continue

        if not (0 <= new_row < size and 0 <= new_column < size):
            print("You cannot move outside the map.")
            continue

        player_row = new_row
        player_column = new_column
        turn += 1

        if player_row == treasure_row and player_column == treasure_column:
            print("\nCongratulations! You found the treasure!")
            return

    print("\nGame over! You ran out of turns.")
    print(
        f"The treasure was at row {treasure_row + 1}, "
        f"column {treasure_column + 1}."
    )


treasure_hunt()