
import pandas as pd
from Model import random_forest
from Model import SVM_cross_validation
from Model import logistic
import os
import csv

def main():
    df = pd.read_csv("temp_afterFeatureEngineering.csv")
    SVM_cross_validation(df)
    # for i in (1,3):
    #     a = csv.writer(open('results%s.csv', 'wb') % i)
    #     a.writerow(['Accuracy_Logistic','Precision_Logistic','F-measure_Logistic','Accuracy_SVM','Precision_SVM','F-measure_SVM', 'Accuracy_RF','Precision_RF','F-measure_RF'])
    #
    #     for k in (1,300,10):
    #         os.system("Dynamic_data_creation.py -K %s -I %s -V Nottingham -R 150 -W 2 -T Pakistan -TP Pakistan -TO England") % (k,i)
    #         os.system("Feature_Engineering.py")
    #
    #         [AL,PL,FL]=logistic(df)
    #         [AR,PR,FR] =random_forest(df)
    #         [AS,PS,FS]=SVM_cross_validation(df)
    #         data = [AL,PL,FL,AR,PR,FR,AS,PS,FS ]
    #         a.writerows(data)


if __name__ =='__main__':
    main()
