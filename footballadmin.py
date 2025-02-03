print("Welcome to the Football Admin Dialogue page...")
home_team = input("what is the name of the home team? \n").title()
away_team = input("what is the name of the away team? \n").title()
while True:
    match_status = input("What is the match status? \n").lower()
    pl_stat = "played"
    sus_stat = "suspended"
    can_stat = "cancelled"

    if match_status == pl_stat:
        home_score = input("What is the score of the home team? \n")
        away_score = input("What is the score of the away team? \n")
        if home_score.isnumeric() and away_score.isnumeric():
            home_score = int(home_score)
            away_score = int(away_score)
            if home_score > away_score:
                print(f"{home_team} won their game against {away_team} by {home_score}:{away_score}")
            elif home_score < away_score:
                print(f"{home_team} lost their game against {away_team} by {home_score}:{away_score}")
            elif home_score == away_score:
                print(f"{home_team} and {away_team} played a {home_score}:{away_score} draw")
            else:
                print(f"The game between{home_team} and {away_team} ended goalless!")
            break
        else:
            print("You have entered invalid scores, try again")
    elif match_status in [can_stat, sus_stat]:
        print(f"The match between {home_team} and {away_team} got {match_status}!")
    else:
        print("Your input is invalid, please try again")
    retry_prompt = input("Would you like to try again? Yes or No: ").title()
    if retry_prompt != "Yes":
        print("Exiting the Football Admin dialogue page. Goodbye!")
        break