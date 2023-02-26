from Data.DataEditor import getData, mean_std
import numpy as np


class EfficientFrontier:

    def pf_performance(self, stocks, weights):
        '''
        :param stocks:
        :param weights:
        :return:
        '''
        meanReturns, covMatrix = mean_std(stocks)
        returns = np.sum(meanReturns * weights) * 252
        std = np.sqrt(np.dot(weights.T, np.dot(covMatrix, weights))) * np.sqrt(252)
        return returns, std

