import statsmodels.api as sm
from sklearn import cross_validation as cv
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
from sklearn.linear_model import LogisticRegression


# def logistic(df):
#     train_cols = df.columns[1:]
#     logit = sm.Logit(df['Won'], df[train_cols])
#     result = logit.fit()
#     print df.describe()


def SVM_cross_validation(df):
    clf = svm.SVC(kernel='linear', C=1)
    df_target = df["Won"]
    df = df.drop('Won', 1)
    scores = cv.cross_val_score(clf, df,df_target , cv=10)
    print scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


def random_forest(df):
    df_target = df["Won"]
    df = df.drop('Won', 1)
    rf = RandomForestClassifier(n_estimators=600)
    scores = cv.cross_val_score(rf, df,df_target , cv=10)
    print scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def logistic (df):
    df_target = df["Won"]
    df = df.drop('Won', 1)
    logistic = LogisticRegression()
    scores = cv.cross_val_score(logistic, df,df_target , cv=10)
    print scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

