
from scipy import stats
import numpy as np

a = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])
# как искать моду
m = stats.mode(a)
print('Мода')
print(m)
# как искать медиану
print('Медиана')
m = np.median(a)
print(m)
# как искать среднее значение
print('Среднее арифметическое')
m = np.mean(a)
print(m)