import pyedflib
import numpy as np
import matplotlib.pyplot as plt


f = pyedflib.EdfReader('C:\\Users\\Lenovo\\Documents\\Analisis Deret Waktu\\RSTUDIO\\DATA\\INPUT\\PRAKTIKUM 1\\S001R01.edf')
n=f.signals_in_file 
signal_labels=f.getSignalLabels()
sigbufs=np.zeros((n, f.getSignalLabels()[0])) 
fig=plt.figure()
ax=plt.axes() 
for i in np.arange(n):
    sigbufs[i, :] = f.readSignal(i) 
    ax.plot(f.readSignal(i))
    x.plot(f.readSignal(i)) 
    plt.show()
    