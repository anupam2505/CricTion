import pandas as pd
from Model import logistic
from Model import SVM_cross_validation
from Feature_Engineering import main as fe



def main():
    #fe();
    df = pd.read_csv('temp_afterFeatureEngineering.csv')
    #logistic(df)
    SVM_cross_validation(df)


if __name__ =='__main__':
    main()
