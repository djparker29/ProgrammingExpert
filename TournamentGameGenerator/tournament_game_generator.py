def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))

        if num_teams >= 2:
            return num_teams

        print("The minimum number of teams is 2, try again.")


def get_team_names(num_teams):
    team_names = []
    for i in range(num_teams):
        while True:
            team_name = input(f"Enter the name for the team #{i + 1}: ")

            if len(team_name) < 2 and len(team_name.split()) <= 2:
                print("Team names must have at least 2 characters, try agian.")
            elif len(team_name.split()) > 2:
                print("team names may have ay most 2 words, try again.")
            else:
                team_names.append(team_name)
                break

    return team_names 

def get_number_of_games_played(num_teams):
    while True:
        games_played = int(input("Enter the number of games played by each team: "))

        if games_played >= num_teams - 1:
            return games_played

        print("Invalid numebr of games.  Each team plays each other at least once int he regular season, try again.")

def get_team_wins(team_names, games_played):
    team_wins = {}

    for team in team_names:
        while True:
            num_wins = int(input(f"Enter the number of wins Team {team} had: "))

            if num_wins < 0:
                print("The minimum number of wins is 0, try again.")
            elif num_wins > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
            else:
                team_wins[team] = num_wins
                break

    return team_wins

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")

ranked_teams = sorted(team_names, key=lambda x: team_wins[x])
for i in range(num_teams //2):
    home_team = ranked_teams[i]
    away_team = ranked_teams[len(team_names) - i - 1]
    print(f"Home: {home_team} VS Away: {away_team}")