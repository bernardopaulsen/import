import bacen as bc
import matplotlib.pyplot as plt

a = bc.bacen('PTAX', 1, '01/01/2000', '12/12/2019')

plt.plot(a)
plt.show()
