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

def main():
    parser = parse_arguments()
    args = parser.parse_args()
    folder_path = args.folder
    dest_folder_path = args.destination_folder


    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f)
        with open(file_path, "w") as f:
            data = json.loads(f)
            file_name = ntpath.basename(str(file_path)).split('.')[0]
            destf = csv.writer(open("%s/%s.csv" % dest_folder_path % file_name, "w", "wb+"))
            run =0;
            wickets =0;
            destf.writerow(["Date","Venue","Balls", "Runs", "Wickets", "Toss", "DN","RPO", "Team1", "Team2", "Team_Won"])
            for i in data['innings'][0]["1st innings"]["deliveries"]:
                day = data["meta"]["created"]["day"]
                month= data["meta"]["created"]["month"]
                year = data["meta"]["created"]["year"]
                date =datetime.datetime.strptime(day+month+year, "%d%m%Y").date()
                venue = data["info"]["city"]
                ballkey = i.keys()[0]
                ballstr = i.keys()[0].split('.')
                ball = ballstr[0]*6 + ballstr[1]
                run = run + i[i.keys()[0]]["runs"]["total"]



if __name__ =='__main__':
    main()
