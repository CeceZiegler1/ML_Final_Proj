import numpy as np

class LinearRegressionAnalytic:
    def __init__(self):
        self.w = None
        
    def fit(self, X, y):
        X_ = self.pad(X)

        #initializing weight vector
        w = np.random.random((X_.shape[1]-1))
        self.w = w
        
        self.alpha = 5

        #Regularizing weight vector
        I = np.eye(X_.shape[1])
        # Don't regularize the bias term to avoid underfitting
        I[0, 0] = 0 
        self.w = np.linalg.inv(X_.T@X_ + self.alpha*I)@X_.T@y
        
    def pad(self, X): #I give credit for this method to the help section of the assignment page
        return np.append(X, np.ones((X.shape[0], 1)), 1)

    def predict(self, X, w): # I give credit for this method to the class notes from 2/20

        '''takes in a feature matrix X, weight vector w, returns the the dot product of the two'''

        X_ = self.pad(X)
        return X_@w
        
    def score(self, X, y):

        '''input: feature matrix X and target vector y

        output: this method returns a float that is the value of the score

        the method computes the score using the formula we calculated in our notes in class'''

        y_hat = self.predict(X,self.w)
        return 1- ((np.sum((y_hat-y)**2))/(np.sum((y-y.mean())**2)))


# Implementing RFE function
def rfe(X, y, k):

    '''
    Input: Feature matrix, X
           Target vector, y
           Number of features to select, int, k

    Returns: A list of indicies corresponding to the selected features

    This method performs a recursive reature elimination using the above implemented
    linear regression method that includes L2 regularization
    
    '''

    if X.shape[1] < k:
        raise ValueError("Not enough features to select.")

    lr = LinearRegressionAnalytic()
    # initialize the set of selected features to be empty
    selected = set()
    # initialize the set of remaining features to be all the features
    remaining = set(range(X.shape[1]))
    # iterate k times
    for i in range(k):
        # compute the optimal weights for each remaining feature
        weights = {}
        for j in remaining:
            features = list(selected) + [j]
            X_subset = X.iloc[:, features]
            lr.fit(X_subset, y)
            weights[j] = lr.w
        # select the feature with the smallest absolute weight
        best_feature = min(weights, key=lambda x: abs(weights[x][-1]))
        # add the best feature to the set of selected features
        selected.add(best_feature)
        # remove the best feature from the set of remaining features
        remaining.remove(best_feature)
    # return the indices of the selected features
    return list(selected)


