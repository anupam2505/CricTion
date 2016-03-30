import json
import csv
import argparse
import os
import ntpath
import datetime

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder',
                        action='store',
                        required='true',
                        help='Path to the directory of json files to parse')
    parser.add_argument('-d', '--destination_folder',
                        action='store',
                        required='true',
                        help='Path to the directory where we want to store csv')
    return parser

def main():
    parser = parse_arguments()
    args = parser.parse_args()
    folder_path = args.folder
    dest_folder_path = args.destination_folder


    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f)

        with open(file_path) as jsonf:
            data = json.load(jsonf)
            try:
                file_name = ntpath.basename(str(file_path)).split('.')[0]
                destf = csv.writer(open("%s/%s_1.csv" % (dest_folder_path , file_name), "wb+"))
                print file_name
                run =0;
                wickets =0;

                #1st Innings
                destf.writerow(["Date","Venue","Balls", "Runs", "Wickets", "Toss", "Team_Playing","RPO", "Team1", "Team2", "Team_Won"])
                for i in data['innings'][0]["1st innings"]["deliveries"]:
                    day = int(data["info"]["dates"][0]["day"])
                    month= int(data["info"]["dates"][0]["month"])
                    year = int(data["info"]["dates"][0]["year"])
                    date = datetime.datetime(year=year, month=month, day=day).date()
                    if "city" in data["info"].keys():
                        venue = data["info"]["city"]
                    else:
                        venue = "No Info"
                    ballstr = i.keys()[0].split('.')
                    if (int(ballstr[1])>=7):
                        ball = int(ballstr[0])*6 + int(6)
                    else:
                        ball = int(ballstr[0])*6 + int(ballstr[1])
                    run = run + i[i.keys()[0]]["runs"]["total"]
                    if 'wicket' in i[i.keys()[0]].keys():
                        wickets = wickets+1
                    toss = data["info"]["toss"]["winner"]
                    team_playing = data['innings'][0]["1st innings"]["team"]
                    RPO = int(run*6)/int(ball)
                    team1 = data['innings'][0]["1st innings"]["team"]
                    team2 = data['innings'][1]["2nd innings"]["team"]
                    if "winner" in (data["info"]["outcome"]).keys():
                        team_won = data["info"]["outcome"]["winner"]
                    else:
                        team_won = "No Result"
                    destf.writerow([date, venue, ball, run, wickets, toss, team_playing, RPO, team1, team2, team_won] )

                # 2nd Innings
                destf = csv.writer(open("%s/%s_2.csv" % (dest_folder_path , file_name), "wb+"))
                run =0;
                wickets =0;
                destf.writerow(["Date","Venue","Balls", "Runs", "Wickets", "Toss", "Team_Playing","RPO", "Team1", "Team2", "Team_Won"])
                for i in data['innings'][1]["2nd innings"]["deliveries"]:
                    day = int(data["info"]["dates"][0]["day"])
                    month= int(data["info"]["dates"][0]["month"])
                    year = int(data["info"]["dates"][0]["year"])
                    date = datetime.datetime(year=year, month=month, day=day).date()
                    if "city" in data["info"].keys():
                        venue = data["info"]["city"]
                    else:
                        venue = "No Info"
                    ballstr = i.keys()[0].split('.')
                    if (int(ballstr[1])>=7):
                        ball = int(ballstr[0])*6 + int(6)
                    else:
                        ball = int(ballstr[0])*6 + int(ballstr[1])
                    run = run + i[i.keys()[0]]["runs"]["total"]
                    if 'wicket' in i[i.keys()[0]].keys():
                        wickets = wickets+1
                    toss = data["info"]["toss"]["winner"]
                    team_playing = data['innings'][1]["2nd innings"]["team"]
                    RPO = int(run*6)/int(ball)
                    team1 = data['innings'][0]["1st innings"]["team"]
                    team2 = data['innings'][1]["2nd innings"]["team"]
                    if "winner" in (data["info"]["outcome"]).keys():
                        team_won = data["info"]["outcome"]["winner"]
                    else:
                        team_won = "No Result"
                    destf.writerow([date, venue, ball, run, wickets, toss, team_playing, RPO, team1, team2, team_won] )
            except:
                pass

if __name__ =='__main__':
    main()
