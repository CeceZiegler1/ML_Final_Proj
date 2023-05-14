import numpy as np
from sklearn import tree


class RandomForest:
    def __init__(self):
        pass

    def fit(self, X, y, k, N):
        self.trees = []
        for i in range(k):
            bootstrap = np.random.choice(X.shape[0], size=N, replace=True)
            
            X_ = X.iloc[bootstrap]
            y_ = y.iloc[bootstrap]

            dtree = tree.DecisionTreeRegressor()
            dtree.fit(X_, y_)
            self.trees.append(dtree)

    def predict(self, X):
        predictions = []
        for tree in self.trees:
            predictions.append(tree.predict(X))
        return np.mean(predictions, axis=0)

    def score(self, X, y):
        predictions = self.predict(X)
        return 1 - np.sum((predictions - y)**2) / np.sum((y - np.mean(y))**2)
