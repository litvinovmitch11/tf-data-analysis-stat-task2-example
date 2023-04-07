import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1126582397 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return (min(x)/7)*(1/np.sqrt(expon(x.size/2).ppf(alpha / 2))), \
           (min(x)/7)*(1/np.sqrt(expon(x.size/2).ppf(1 - alpha / 2)))
