import yaml
import json
import argparse
import os
import datetime
import ntpath

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder',
                        action='store',
                        required='true',
                        help='Path to the directory of yaml files to parse')
    return parser

def jdefault(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__

def main():
    parser = parse_arguments()
    args = parser.parse_args()
    folder_path = args.folder


    for f in os.listdir(folder_path):
        python_path = os.path.join(folder_path, f)
        with open(python_path, 'r') as stream:
            file_name = (ntpath.basename(str(python_path)).split('.'))[0]
            try:
                data = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
            with open("Json_Data/%s.json" % file_name, "w") as f:
                f.write(json.dumps(data, f, ensure_ascii=False, default=jdefault).encode('utf-8'))
                print(json.dumps(data, f, ensure_ascii=False, default=jdefault).encode('utf-8'))

##  For MAC users - Add argument like this -f "Data/odis"
##  For Window users - Add argument like this -f "Data\\odis`"


if __name__ == '__main__':
    main()

