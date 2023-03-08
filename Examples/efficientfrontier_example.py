from Portfolio.Portfolio import PortfolioManager
from Data.DataEditor import getData, mean_std
import numpy as np



def main():



    mean_returns = np.array([1.5, 3, 2])
    print(mean_returns.shape[0])
    cov_Matrix = np.ones((3, 3)
    )
    weights = np.array([0.4, 0.3, 0.3])
    pf_manager = PortfolioManager(weights=weights, mean_returns=mean_returns, cov_Matrix=cov_Matrix)
    print(pf_manager.pf_Performance)
    results = pf_manager.maxPF_SharpeRatio(riskfree_rate=0, constraintSet=(0, 1))
    print(results)



if __name__ == '__main__':
        main()