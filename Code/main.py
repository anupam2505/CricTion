
import pandas as pd
from Model import random_forest
from Model import SVM_cross_validation
from Model import logistic
import os
import csv
import subprocess
from Dynamic_data_creation import create_dataset
import Feature_Engineering as fe
import sys


def main():
    file_path = os.getcwd()

    for i in range(1,3):
        print "i value %s" % str(i)
        file = 'results %s.csv' % str(i)
        a = csv.writer(open(file, 'wb'))
        final_data = []
        a.writerow(['Balls','Accuracy_Logistic','Precision_Logistic','F-measure_Logistic','Accuracy_SVM','Precision_SVM','F-measure_SVM', 'Accuracy_RF','Precision_RF','F-measure_RF'])

        for k in range(10,300,10):
            try:
                print k
                create_dataset(str(k),str(i))

                df1 = fe.main()
                df = pd.read_csv("temp_afterFeatureEngineering.csv")
                AL, PL, FL =logistic(df)
                #print AL, PL, FL
                [AS,PS,FS]=SVM_cross_validation(df)
                [AR,PR,FR] =random_forest(df)
                data = [str(k),AL, PL, FL, AS,PS,FS,AR,PR,FR]
                final_data.append(data)
                print data
            except:
                print "Unexpected error:", sys.exc_info()[0]
        print final_data
        a.writerows(final_data)


if __name__ =='__main__':
    main()
