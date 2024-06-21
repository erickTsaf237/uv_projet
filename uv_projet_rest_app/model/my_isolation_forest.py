from sklearn.ensemble import IsolationForest

def getTrainIsolatedForestModel(X):
    model = IsolationForest()
    model.fit(X)
    return model