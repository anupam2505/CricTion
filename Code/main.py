
import pandas as pd
from Model import random_forest
from Model import SVM_cross_validation
from Model import logistic

def main():
    #fe();
    df = pd.read_csv('temp_afterFeatureEngineering.csv')
    #logistic(df)
    #random_forest(df)
    SVM_cross_validation(df)


if __name__ =='__main__':
    main()
