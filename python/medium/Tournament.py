"""Tournament

https://exercism.org/tracks/python/exercises/tournament

@yawpitch has a really nice solution to this
https://exercism.org/tracks/python/exercises/tournament/solutions/yawpitch
"""


def tally(matches: list[str]) -> list[str]:
    """Format a list of raw match data into a nice-looking score table.
    
    :param matches: - Raw match data where each match is represented as:
                      team one;team two;match result.
    :return table: - A nicely formatted table displaying the results of the matches.
    """
    match_history = [match.split(";") for match in matches]
    season = {}
    table = [f"{'Team':<30} | {'MP':>2} | {'W':>2} | {'D':>2} | {'L':>2} | {'P':>2}"]

    # scoring logic
    #  MP = matches played
    #  W  = matches won
    #  D  = matches drawn
    #  L  = matches lost
    #  P  = points earned from matches won and drawn
    for match in match_history:
    # for home, away, match in match_history:
        for team in match[:2]:
            if team not in season:
                season[team] = {
                    "MP": 0,
                    "W": 0,
                    "D": 0,
                    "L": 0,
                    "P": 0,
                }
            season[team]["MP"] += 1
        
        if match[2] == "win":
            season[match[0]]["W"] += 1
            season[match[1]]["L"] += 1
            season[match[0]]["P"] += 3
                    
        elif match[2] == "loss":
            season[match[0]]["L"] += 1
            season[match[1]]["W"] += 1
            season[match[1]]["P"] += 3
                    
        elif match[2] == "draw":
            season[match[0]]["D"] += 1
            season[match[1]]["D"] += 1
            season[match[0]]["P"] += 1
            season[match[1]]["P"] += 1

    # preserve the table header; the first row in the table
    rows = []
    for team in sorted(season): # alph sort teams
        row = (
            f'{team:<30} '
            f'| {season[team]["MP"]:>2} '
            f'| {season[team]["W"]:>2} '
            f'| {season[team]["D"]:>2} '
            f'| {season[team]["L"]:>2} '
            f'| {season[team]["P"]:>2}'
        )
        rows.append(row)

    # 52'nd index of each row is where xxx points begin
    rows.sort(key=lambda x: x[52:], reverse=True) # point sort teams

    # construct and return formatted score table
    for row in rows:
        table.append(row)
    
    return table
