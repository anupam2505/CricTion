import statsmodels.api as sm
from sklearn import cross_validation
from sklearn import svm

def logistic(df):
    train_cols = df.columns[1:]
    logit = sm.Logit(df['Won'], df[train_cols])
    result = logit.fit()
    print df.describe()

def cross_validation(df):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(df, df["Won"], test_size=0.1, random_state=0)
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    clf.score(X_test, y_test)


