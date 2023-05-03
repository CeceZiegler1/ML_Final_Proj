import numpy as np

class LinearRegressionAnalytic():

    def __init__(self, fit_intercept=True):
        self.fit_intercept = fit_intercept

    def pad(self, X): #I give credit for this method to the help section of the assignment page
        return np.append(X, np.ones((X.shape[0], 1)), 1)

    def predict(self, X, w): # I give credit for this method to the class notes from 2/20

        '''takes in a feature matrix X, weight vector w, returns the the dot product of the two'''

        X_ = self.pad(X)
        return X_@w

    def fit(self, X, y):

        '''Input: Feature matrix, X and target vector, y, returns nothing

        This method computes the value of the weight vector, w, using the analytical formula
        we calculated in class. It then computes the score and keeps track of the score history
        with an array'''

        X_ = self.pad(X)
        w = np.random.random((X_.shape[1]-1))#initializing weight vector
        self.w = w

        self.w = np.linalg.inv(X_.T@X_)@X_.T@y #updating w using analytical formula
        self.coef_ = self.w[:-1] # Set coef_ attribute to the weight vector, excluding the bias term

    def score(self, X, y):

        '''input: this method takes in the feature matrix X and target vector y

        output: this method returns a float that is the value of the score

        the method computes the score using the formula we calculated in our notes in class'''

        y_hat = self.predict(X,self.w)
        return 1- ((np.sum((y_hat-y)**2))/(np.sum((y-y.mean())**2)))

    def get_params(self, deep=True):
        return {'fit_intercept': self.fit_intercept}

