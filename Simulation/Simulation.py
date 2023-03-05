import numpy as np
import matplotlib.pyplot as plt



class SimulatorManager:
    def __init__(self, NoOfPaths=10, NoOfSteps=1000):
        self.NoOfPaths = NoOfPaths
        self.NoOfSteps = NoOfSteps

    def update_noOfPathsnSteps(self, NoOfPaths, NoOfSteps):
        self.NoOfSteps = NoOfSteps
        self.NoOfPaths = NoOfPaths


    def GeneratePathsGBMABM(self, T, r, sigma, S_0):

        # Fixing random seed
        np.random.seed(1)

        Z = np.random.normal(0.0, 1.0, [self.NoOfPaths, self.NoOfSteps])
        X = np.zeros([self.NoOfPaths, self.NoOfSteps + 1])
        S = np.zeros([self.NoOfPaths, self.NoOfSteps + 1])
        time = np.zeros([self.NoOfSteps + 1])

        X[:, 0] = np.log(S_0)

        dt = T / float(self.NoOfSteps)
        for i in range(0, self.NoOfSteps):
            # making sure that samples from normal have mean 0 and variance 1
            if self.NoOfPaths > 1:
                Z[:, i] = (Z[:, i] - np.mean(Z[:, i])) / np.std(Z[:, i])

            X[:, i + 1] = X[:, i] + (r - 0.5 * sigma ** 2) * dt + sigma * np.power(dt, 0.5) * Z[:, i]
            time[i + 1] = time[i] + dt

        # Compute exponent of ABM
        S = np.exp(X)
        paths = {"time": time, "X": X, "S": S}
        return paths


    def discountValue(self, S, r, t):

        # Discounted Stock paths
        S_disc = np.zeros([self.NoOfPaths, self.NoOfSteps + 1])
        M = lambda t: np.exp(r * t)

        for i, ti in enumerate(t):
            S_disc[:, i] = S[:, i] / M(ti)

        return S_disc



    def plot_paths(self, Paths: dict):
        try:
            timeGrid = Paths["time"]
            X = Paths["X"]
            S = Paths["S"]

            plt.figure(1)
            plt.plot(timeGrid, np.transpose(X))
            plt.grid()
            plt.xlabel("time")
            plt.ylabel("X(t)")

            plt.figure(2)
            plt.plot(timeGrid, np.transpose(S))
            plt.grid()
            plt.xlabel("time")
            plt.ylabel("S(t)")

        except:
            print('Paths must be a dict with X, S and time as keys!')

    
