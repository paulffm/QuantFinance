import numpy as np
from scipy.stats import norm
N = norm.cdf
class BlackScholes:
    def __init__(self, S, K, T, r, sigma, q=0):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.q = q

    def calcCall(self):
        d1 = (np.log(self.S / self.K) + (self.r - self.q + self.sigma ** 2 / 2) * self.T) / \
             (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return self.S*np.exp(-self.q*self.T)*N(d1) - self.K*np.exp(-self.r*self.T) * N(d2)

    def calcPut(self):
        d1 = (np.log(self.S / self.K) + (self.r - self.q + self.sigma ** 2 / 2) * self.T) / \
             (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return self.K*np.exp(-self.r*self.T) * N(-d2) - self.S*np.exp(-self.q*self.T)*N(-d1)



