import scipy.stats as st
import numpy as np


class MyTestDistribution(st.rv_continuous):
    def _pdf(self, x, *args):
        return np.exp(-x**2 /2.)/np.sqrt(2.0 * np.pi)

