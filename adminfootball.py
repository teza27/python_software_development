print("Welcome to the Football Admin Dialogue page...")
home_team = input("What is the name of the home team?\n").title()
away_team = input("What is the name of the away team?\n").title()

while True:
    match_status = input("What is the status of the match?\n").lower()
    pl_stat = "played"
    sus_stat = "suspended"
    can_stat = "cancelled"

    if match_status == pl_stat:
        home_score = input("How many goals was scored by the home team?\n")
        away_score = input("How many goals was scored by the away team?\n")
        if home_score.isnumeric() and away_score.isnumeric():
            home_score = int(home_score)
            away_score = int(away_score)
            if home_score > away_score:
                print(f"{home_team} won their match against {away_team} by {home_score}:{away_score}.")
            elif home_score < away_score:
                print(f"{home_team} lost their match against {away_team} by {home_score}:{away_score}.")
            elif home_score == away_score:
                print(f"The match between {home_team} and {away_team} ended in {home_score}:{away_score} draw.")
            else:
                print(f"The match between {home_team} and {away_team} ended in a goalless draw.")
            break
        else:
            print("You need to provide the score in integer.")
    elif match_status in [sus_stat, can_stat]:
        print(f"The match between {home_team} and {away_team} was {match_status}.")
    else:
        print("You have provided an invalid response")
    retry = input("Would you like to retry the match status? Yes or No:\n").title()
    if retry != "Yes":
        print("Exiting the Football Admin dialogue. Goodbye!")
        break