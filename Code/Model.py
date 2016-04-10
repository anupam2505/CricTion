import statsmodels.api as sm
from sklearn import cross_validation as cv
from sklearn import svm

def logistic(df):
    train_cols = df.columns[1:]
    logit = sm.Logit(df['Won'], df[train_cols])
    result = logit.fit()
    print df.describe()

def SVM_cross_validation(df):
    clf = svm.SVC(kernel='linear', C=1)
    df_target = df["Won"]
    df = df.drop('Won', 1)
    scores = cv.cross_val_score(clf, df,df_target , cv=2)
    print scores
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


    # predicted = cv.cross_val_predict(clf, df,df["Won"], cv=10)
    # print metrics.accuracy_score(df["Won"], predicted)
    # X_train, X_test, y_train, y_test = cv.train_test_split(df, df["Won"], test_size=0.1, random_state=0)
    # clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    # print clf.score(X_test, y_test)


