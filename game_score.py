def main():
    # Input Collection
    player_name = input("Enter player's name: ")
    
    # Numeric Input Processing
    try:
        games_played = int(input("Enter number of games played: "))
        total_score = int(input("Enter total score: "))
    except ValueError:
        print("Error: Please enter valid integers for games played and score.")
        return

    # Computation
    if games_played > 0:
        average_score = total_score / games_played
    else:
        average_score = 0.0

    # Output Display
    print(f"\nPlayer: {player_name}")
    print(f"\nGames Played: {games_played}")
    print(f"\nTotal Score: {total_score}")
    print(f"\nAverage Score: {average_score}")

if __name__ == "__main__":
    main()
