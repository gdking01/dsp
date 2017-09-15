# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd
footy = pd.read_csv(football.csv)
footy["Diff"]=[abs(x-y) for x,y in zip(footy.Goals, footy["Goals Allowed"])]
whichsmallest = footy.Diff[footy.Diff==min(footy.Diff)].index[0]
print(footy.Team[whichsmallest])
