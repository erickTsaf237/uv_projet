import numpy as np;
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest
import numpy as np

def getTrainIsolatedForestModel(train_X, test_X):
    """
    Entraîne un modèle Isolation Forest et évalue les résultats sur un jeu de test.
    
    Args:
        train_X (numpy.ndarray): Tableau numpy des données d'entraînement.
        test_X (numpy.ndarray): Tableau numpy des données de test.
        
    Returns:
        int: Somme des prédictions du modèle sur le jeu de test.
    """
    # Vérification du type des entrées
    if not isinstance(train_X, np.ndarray) or not isinstance(test_X, np.ndarray):
        raise TypeError("train_X et test_X doivent être des tableaux numpy.")
    
    # Entraînement du modèle
    model = IsolationForest()
    model.fit(train_X)
    
    # Évaluation sur le jeu de test
    test_predictions = model.predict(test_X)
    return int(test_predictions.sum())


def getTrainIsolatedForestModel(train_X, test_X):
    model = IsolationForest()
    model.fit(train_X)
    return model.predict(test_X).sum()


data = np.array( [ [ 22.185,  34.425,  52.53,   12.24,   30.345], [ 18.105,  59.16,   83.385,  41.055,  65.28 ] ,       [ 24.225,  81.855, 105.825,  57.63,   81.6,  ] ,       [ 23.97,   56.61,   79.05,   32.64 ,  55.08 ]       , [ 22.44,   61.2,    93.84 ,  38.76 ,  71.4  ] ,       [ 32.64 ,  49.215,  73.44 ,  16.575,  40.8  ] ,       [ 24.225 , 83.64 , 105.825,  59.415 , 81.6  ]  ,      [ 22.185, 136.425 ,156.825 ,114.24 , 134.64 ]     ,   [ 20.4 ,   69.36 , 100.215 , 48.96 ,  79.815],        [ 30.855 , 49.215 , 73.44  , 18.36  , 42.585]      ,  [ 24.225 ,116.28 , 126.225 , 92.055 ,102.   ]  ,      [  9.945 ,148.92 , 169.32 , 138.975, 159.375] ,       [ 20.4 ,   52.785 , 79.305  ,32.385 , 58.905]      ,  [ 26.52  , 77.775 ,114.24 ,  51.255 , 87.72 ]      ,  [ 36.465 ,179.52,  213.945 ,143.055 ,177.48 ] ,       [ 34.425 , 97.92 , 113.985 , 63.495 , 79.56 ] ,       [ 16.065 , 46.92 ,  67.065 , 30.855 , 51.   ]      ,  [ 20.145, 118.32 , 140.505 , 98.175, 120.36 ] ,       [ 22.185,  48.96 ,  73.185 , 26.775 , 51.   ]      ,  [ 24.225  ,56.865  ,85.425 , 32.64 ,  61.2  ]  ,      [ 28.56  , 75.48 , 102.255 , 46.92  , 73.695]     ,   [ 26.775 , 53.55  , 75.48 ,  26.775 , 48.705]     ,   [ 21.93,  144.585 ,179.01 , 122.655 ,157.08 ] ,       [ 34.425 , 85.68 , 107.865 , 51.255 , 73.44 ]     ,   [ 22.185 ,104.04,  116.025 , 81.855 , 93.84 ]     ,   [ 11.985,  55.08 ,  83.385 , 43.095,  71.4  ] ,       [ 28.305 , 95.88 , 120.36  , 67.575 , 92.055]])
test_data = np.array( [ [ 22.185,  37.425,  52.53,   12.24,   3.345], [ 18.105,  59.16,   81.385,  40.055,  65.08 ] ,       [ 12.225,  81.855, 10.825,  57.63,   89.6,  ] ,       [ 93.97,   16.61,   9.05,   22.64 ,  15.08 ]       , [ 22.44,   61.2,    93.84 ,  38.76 ,  71.4  ] ,      ])


#print(data[:, 0:1])

#plt.scatter(range(len(data[:, 0:1][0])), data[:, 0:1][0])
#plt.imshow(np.random.randint(0, 255, 7*10).reshape(7, 10), cmap='grey')
#plt.show()

la_en = LabelEncoder()
#print(la_en.fit_transform(['yi', 'je suis']), la_en.fit_transform(['bomjour']))
print(getTrainIsolatedForestModel(data, test_data))

la_en = LabelEncoder()

#print (help(la_en.fit_transform))

#print(help(hash))