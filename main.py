import math

# from Charts import *

# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


class Calculation:
    def __init__(self, n, p):
        q = 1 - p
        if (n * p - q) == int(n * p - q):
            self.k = int(n * p - q)
        else:
            self.k = math.ceil(n * p - q)


if __name__ == "__main__":
    n = 300
    p = 0.75
    calculation = Calculation(n, p)
    print(calculation.k)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
