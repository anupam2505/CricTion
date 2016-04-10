import pandas as pd
from Model import logistic
from Model import cross_validation


def main():
    df = pd.read_csv('temp_afterFeatureEngineering.csv')
    #logistic(df)
    cross_validation(df)


if __name__ =='__main__':
    main()
