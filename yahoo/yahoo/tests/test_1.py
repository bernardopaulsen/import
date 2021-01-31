import matplotlib.pyplot as plt
import yahoo as yh

a = yh.yahoo('PETR4.SA', (2000,1,1), (2019,12,12))

plt.plot(a['Ret'])
plt.show()