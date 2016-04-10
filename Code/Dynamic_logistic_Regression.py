import argparse
import csv
import os
from collections import namedtuple
from contextlib import closing



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-K', '--Balls_Bowled',
                        action='store',
                        required='true',
                        help='Number of bowls bowled')
    parser.add_argument('-I', '--Innings',
                        action='store',
                        required='true',
                        help='Innning = 1 or Innning = 2')

    parser.add_argument('-V', '--Venue',
                        action='store',
                        required='true',
                        help='Venue of the match')

    parser.add_argument('-R', '--Runs',
                        action='store',
                        required='true',
                        help='Runs scored till now')

    parser.add_argument('-W', '--Wickets',
                        action='store',
                        required='true',
                        help='Wickets lost till now')

    parser.add_argument('-T', '--Toss',
                        action='store',
                        required='true',
                        help='Which team won toss')

    parser.add_argument('-TP', '--Team_Playing',
                        action='store',
                        required='true',
                        help='Which team is bating')

    parser.add_argument('-TO', '--Team_Opponent',
                        action='store',
                        required='true',
                        help='Which team is bowling')

    ##"Venue","Balls", "Runs", "Wickets", "Toss", "Team_Playing","RPO", "Team1", "Team2"
    return parser

def main():
    parser = parse_arguments()
    args = parser.parse_args()
    bowls_bowled = args.Balls_Bowled
    inning = args.Innings
    venue = args.Venue
    runs = args.Runs
    wickets = args.Wickets
    toss = args.Toss
    team_playing = args.Team_Playing
    team_against = args.Team_Opponent
    i = create_dataset(bowls_bowled, inning)

def create_dataset(bowls_bowled, inning):
    folderpath = "CSV_Data/%s/" % (inning)
    final_data = []
    for f in os.listdir(folderpath):
        file_path = os.path.join(folderpath, f)
        with open(file_path) as csv_file:
            a = csv.writer(open('temp.csv', 'wb'))
            a.writerow(['Runs','Balls','Toss', 'Venue', 'Team1', 'Team2', 'Wickets','Date', 'RPO', 'Won'])
            # Important features are RPO, Toss, Venue, Team1, Team2, Wickets, RPO, FD
            # Output : Won
            toss=0;
            won=0;
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                if (row["Balls"]==bowls_bowled):
                    if (row["Team_Playing"] == row["Toss"]):
                        toss =1;
                    else:
                        toss=0;
                        if (row["Team_Playing"] == row["Team_Won"]):
                            won =1;
                        else:
                            won=0
                    data = [row["Runs"],row["Balls"], toss, row["Venue"], row["Team1"], row["Team2"],
                            row["Wickets"], row["Date"], row["RPO"], won]
                    final_data.append(data)
                    print data
    print final_data
    a.writerows(final_data)



if __name__ =='__main__':
    main()