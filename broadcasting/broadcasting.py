import numpy as np
prices = np.array([199, 245, 389])
discount=10
new_prices=prices-(prices*discount/100)
print(new_prices)  