
import pandas as pd
from Model import random_forest
from Model import SVM_cross_validation
from Model import logistic
import os

def main():
    for i in (1,3):
        for k in (1,300,10):
            os.system("Dynamic_data_creation.py -K %s -I %s -V Nottingham -R 150 -W 2 -T Pakistan -TP Pakistan -TO England") % (k,i)
            os.system("Feature_Engineering.py")
            
            df = pd.read_csv('temp_afterFeatureEngineering.csv')
            logistic(df)
            random_forest(df)
            SVM_cross_validation(df)


if __name__ =='__main__':
    main()
