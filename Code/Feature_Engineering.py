import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from logistic_regression import logistic

def one_hot_dataframe(data, cols, replace=False):
    """ Takes a dataframe and a list of columns that need to be encoded.
        Returns a 3-tuple comprising the data, the vectorized data,
        and the fitted vectorizor."""
    vec = DictVectorizer(sparse=False)
    vecData = pd.DataFrame(vec.fit_transform(data[cols].T.to_dict().values()))
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    if replace is True:
        data = data.drop(cols, axis=1)
        data = data.join(vecData)
    return (data, vecData, vec)

def main():

    # Get a random DataFrame
    df = pd.read_csv('temp.csv')
    #print df.describe()
    #print (df.columns)
    # Vectorize the categorical columns: e & f
    df, _, _ = one_hot_dataframe(df, ['Team1', 'Team2', 'Venue'], replace=True)
    #print df
    df["RPO"]= df["RPO"]/df["RPO"].max();
    df["Wickets"]= df["Wickets"]/df["Wickets"].max();
    df = df.drop('Runs', 1)
    df = df.drop('Balls', 1)
    df = df.drop('Date', 1)
    logistic(df)

    df.to_csv('temp_afterFeatureEngineering.csv')



