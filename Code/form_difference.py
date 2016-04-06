import csv
import argparse
import os
import ntpath
import datetime
import numpy
import collections

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder',
                        action='store',
                        required='true',
                        help='Path to the directory where we want to store csv')
    return parser

def main():
    parser = parse_arguments()
    args = parser.parse_args()
    folder_path = args.folder
    form1 = collections.deque(maxlen=5)
    form2 = collections.deque(maxlen=5)
    coef = [ (1-0.2041)**(4-i) for i in range(0,5)]

    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f)
        if os.path.isdir(file_path):
            break;
        with open(file_path, 'r') as curr:
            curr_reader = csv.reader(curr)

            data1 = []
            row = next(curr_reader)
            row.append('form_difference')
            data1.append(row)
            try: 
                row = next(curr_reader)
                Team1,Team2 = row[8],row[9]
            except:
                pass
                

            file_name = ntpath.basename(str(f)).split('.')[0]
            with open('CSV_Data/Innings1/'+ file_name + '.csv' ,'w') as newfile:
                writer = csv.writer(newfile)
                # write to file form difference

                for files in os.listdir(folder_path):
                    if files == f:
                        break;
                    f_path = os.path.join(folder_path, files)
                    with open(f_path, 'r') as prev:
                        reader = csv.reader(prev);next(reader)
                        try:
                            line = next(reader)

                            if(Team1 == line[8] or line[9]):
                                form1.append(1) if Team1 == line[10] else form1.append(0)
                            
                            if(Team2 == line[8] or line[9]):
                                form2.append(1) if Team2 == line[10] else form2.append(0)
                        except:
                            pass

                if(len(form1) < 5 or len(form2) < 5):
                    fd1 = None
                    fd2 = None
                else:
                    f1 = numpy.average(form1,0,coef)
                    f2 = numpy.average(form2,0,coef)                   
                    fd1 = round((f1-f2/f1)*100,2)
                    fd2 = round((f2-f1/f2)*100,2)
                
                    row.append(fd1)
                    data1.append(row)
                    for row in curr_reader:
                        row.append(fd1)
                        data1.append(row)

                writer.writerows(data1)

            file2 = str(file_name).split('_')[0] + '_2'
            with open('CSV_Data/Innings2/'+ file2  + '.csv' ,'w') as newfile2:
                writer = csv.writer(newfile2)
                try:
                    with open('CSV_Data/2/'+ file2 + '.csv','r') as inn2file:
                        file2reader = csv.reader(inn2file)
                        data2 = []

                        rowdata = next(file2reader)
                        rowdata.append('form_difference')
                        data2.append(rowdata)

                        for rowdata in file2reader:
                            rowdata.append(fd2)
                            data2.append(rowdata)

                except:
                    pass

                writer.writerows(data2)    

if __name__ == "__main__":
    main()
