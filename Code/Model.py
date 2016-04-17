import statsmodels.api as sm
from sklearn import cross_validation as cv
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
from sklearn.linear_model import LogisticRegression
import metrics

# def logistic(df):
#     train_cols = df.columns[1:]
#     logit = sm.Logit(df['Won'], df[train_cols])
#     result = logit.fit()
#     print df.describe()


def SVM_cross_validation(df):
    clf = svm.LinearSVC(C=10)
    df_target = df["Won"]
    df = df.drop('Won', 1)
    p = cv.cross_val_score(clf, df,df_target , cv=10, scoring='precision').mean()
    r = cv.cross_val_score(clf, df,df_target , cv=10, scoring='recall').mean()
    f =  2 * (p * r) / (p + r)
    # print("Accuracy of SVM: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # return scores.mean(),
    print "SVM Accuracy %s" % str(p)
    return p, r, f

def random_forest(df):
    df_target = df["Won"]
    df = df.drop('Won', 1)
    rf = RandomForestClassifier(n_estimators=100)
    p = cv.cross_val_score(rf, df,df_target , cv=10, scoring='precision').mean()
    r = cv.cross_val_score(rf, df,df_target , cv=10, scoring='recall').mean()
    f =  2 * (p * r) / (p + r)
    # print("Accuracy of SVM: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # return scores.mean(),
    print "RF Accuracy %s" % str(p)
    return p, r, f

def logistic (df):
    df_target = df["Won"]
    df = df.drop('Won', 1)
    df.index.name = None
    logistic = LogisticRegression()
    p = cv.cross_val_score(logistic, df,df_target , cv=10, scoring='precision').mean()
    r = cv.cross_val_score(logistic, df,df_target , cv=10, scoring='recall').mean()
    f =  2 * (p * r) / (p + r)
    # print("Accuracy of SVM: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # return scores.mean(),
    print "LR Accuracy %s" % str(p)
    return p, r, f
