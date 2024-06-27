

import numpy as np
from sklearn.neighbors import  LocalOutlierFactor



def user_local_outlier_factor_test(X_train, X_test):
    lof = LocalOutlierFactor(novelty=True)
    print('-------------------------------------------------------------------------------')
    print(X_train)
    print('-------------------------------------------------------------------------------')
    lof.fit(X_train)
    y_pred = lof.predict(X_test)
    return (y_pred, lof)
