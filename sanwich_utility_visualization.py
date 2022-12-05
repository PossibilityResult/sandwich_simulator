from sandwich_classes import Pool
from matplotlib import pyplot as plt
import numpy as np

def plotSandwicherUtility(_initialR0, _initialR1, _fee):

    pool = Pool(_initialR0, _initialR1, _fee)

    sandwich_in_amounts = np.linspace(0, 100, 100000)

    sandwicher_utilities = np.array([])

    for sandwich_in in sandwich_in_amounts:  
        # amount_in, token_in, token_out
        front_tx = (sandwich_in, 0, 0)
        retail_tx = (3, 0, 0)

        amount_out_front = pool.swap(front_tx[0], front_tx[1], front_tx[2])
        back_tx = (amount_out_front, 1, 0)

        amount_out_swap = pool.swap(retail_tx[0], retail_tx[1], retail_tx[2])

        amount_out_back = pool.swap(back_tx[0], back_tx[1], back_tx[2])

        sandwicher_utilities = np.append(sandwicher_utilities, amount_out_back - sandwich_in)

        pool.resetPool(_initialR0, _initialR1)

    plt.plot(sandwich_in_amounts, sandwicher_utilities)
    plt.title("Sandwicher Utility by Amount in for a Fee: {}".format(_fee))
    plt.xlabel('Sandwich Amount in')
    plt.ylabel('Sandwicher Utility (Denominated in terms of the input Token)')
    plt.show()
