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
            file_name = ntpath.basename(str(file_path)).split('.')[0]
            destf = csv.writer(open("%s/%s.csv" % (dest_folder_path , file_name), "wb+"))
            run =0;
            wickets =0;
            destf.writerow(["Date","Venue","Balls", "Runs", "Wickets", "Toss", "Team_Playing","RPO", "Team1", "Team2", "Team_Won"])
            for i in data['innings'][0]["1st innings"]["deliveries"]:
                day = data["meta"]["created"]["day"]
                month= data["meta"]["created"]["month"]
                year = data["meta"]["created"]["year"]
                date =datetime.datetime.strptime(str(day)+str(month)+str(year), "%d%m%Y").date()
                venue = data["info"]["city"]
                ballstr = i.keys()[0].split('.')
                ball = ballstr[0]*6 + ballstr[1]
                run = run + i[i.keys()[0]]["runs"]["total"]
                if 'wicket' in i.keys():
                    wickets = wickets+1
                toss = data["info"]["toss"]["winner"]
                team_playing = data['innings'][0]["1st innings"]["team"]
                RPO = int(run*6)/int(ball)
                team1 = data['innings'][0]["1st innings"]["team"]
                team2 = data['innings'][1]["2nd innings"]["team"]
                team_won = data["info"]["outcome"]["winner"]
                destf.writerow([date, venue, ball, run, wickets, toss, team_playing, RPO, team1, team2, team_won] )


if __name__ =='__main__':
    main()
