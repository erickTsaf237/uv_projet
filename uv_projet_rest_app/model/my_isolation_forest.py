from sklearn.ensemble import IsolationForest
import numpy as np

 
def getTrainIsolatedForestModel(X):
    model = IsolationForest()
    model.fit(X)
    return model


def test_user(train_X, test_X):
    """
    Entraîne un modèle Isolation Forest et évalue les résultats sur un jeu de test.
    
    Args:
        train_X (numpy.ndarray): Tableau numpy des données d'entraînement.
        test_X (numpy.ndarray): Tableau numpy des données de test.
        
    Returns:
        int: Somme des prédictions du modèle sur le jeu de test.
    """
    # Vérification du type des entrées
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(train_X)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    if not isinstance(train_X, np.ndarray) or not isinstance(test_X, np.ndarray):
        raise TypeError("train_X et test_X doivent être des tableaux numpy.")
    
    # Entraînement du modèle
    model = IsolationForest()
    model.fit(train_X)
    
    # Évaluation sur le jeu de test
    test_predictions = model.predict(test_X)
    return int(test_predictions.sum())