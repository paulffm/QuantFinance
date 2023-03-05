from Data.DataEditor import getData, mean_std
import numpy as np
from scipy import optimize


def calc2_pf_SharpeRatio(w, mean_returns, cov_matrix, risk_freeRate=0):
    pReturns = np.sum(mean_returns * w) * 252
    pStd = np.sqrt(np.dot(w.T, np.dot(cov_matrix, w))) * np.sqrt(252)
    return - (pReturns - risk_freeRate) / pStd
class PortfolioManager:
    def __init__(self, weights, mean_returns, cov_Matrix):
        self.weights = np.array(weights)
        self.meanReturns = np.array(mean_returns)
        self.covMatrix = np.array(cov_Matrix)

    @property
    def pf_Performance(self):
        returns = np.sum(self.meanReturns * self.weights) * 252
        std = np.sqrt(np.dot(self.weights.T, np.dot(self.covMatrix, self.weights))
                      ) * np.sqrt(252)
        return returns, std

    @property
    def pf_Return(self):
        return self.pf_Performance[0]

    @property
    def pf_Variance(self):
        return self.pf_Performance[1]


    '''def pf_SharpeRatio(self, weights, meanReturns, covMatrix, riskFreeRate = 0):
        pfReturns, pfStd = self.pf_Performance(weights, meanReturns, covMatrix)
        return - (pfReturns - riskFreeRate) / pfStd'''

    def pf_SharpeRatio(self, riskFreeRate=0):
        pfReturns, pfStd = self.pf_Performance
        return - (pfReturns - riskFreeRate) / pfStd

    @staticmethod
    def __calc_pf_SharpeRatio(w, mean_returns, cov_matrix, risk_freeRate = 0):
        pReturns = np.sum(mean_returns * w) * 252
        pStd = np.sqrt(np.dot(w.T, np.dot(cov_matrix, w))) * np.sqrt(252)
        return - (pReturns - risk_freeRate) / pStd

    def maxPF_SharpeRatio(self, riskfree_rate=0, constraintSet=(0, 1)):
        '''PortfolioManager.maxPF_SharpeRatio.<locals>.<lambda>() takes 1 positional argument but 4 were given'''
        mean_returns, covMatrix = self.pf_Performance

        numAssets = self.meanReturns.shape[0]
        args = (mean_returns, covMatrix, riskfree_rate)
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bound = constraintSet
        bounds = tuple(bound for asset in range(numAssets))
        m = self.meanReturns
        c = self.covMatrix
        f = lambda w: self.__calc_pf_SharpeRatio(w, mean_returns=m, cov_matrix=c,
                                                 risk_freeRate=riskfree_rate)

        result = optimize.minimize(fun=f, x0=numAssets * [1. / numAssets], args=args, method='SLSQP',
                                   bounds=bounds, constraints=constraints)
        return result



