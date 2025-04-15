import pyedflib
import numpy as np
import matplotlib.pyplot as plt

# Ganti path file dengan path yang sesuai di komputer Anda
file_path = r'C:\\Users\\Lenovo\\Documents\\Analisis Deret Waktu\\RSTUDIO\\DATA\\INPUT\\PRAKTIKUM 1\\S001R01.edf'

# Membuat objek EdfReader untuk membaca file EDF
try:
    f = pyedflib.EdfReader(file_path)
    n = f.signals_in_file
    signal_labels = f.getSignalLabels()
    sigbufs = np.zeros((n, f.getNSamples()[0]))
    
    fig, ax = plt.subplots(n, 1, figsize=(10, 6))
    
    for i in range(n):
        sigbufs[i, :] = f.readSignal(i)
        ax[i].plot(sigbufs[i, :])
        ax[i].set_title(signal_labels[i])
    
    plt.tight_layout()
    plt.show()
    
    # Tutup file setelah selesai membacanya
    f.close()
    
except Exception as e:
    print("Terjadi kesalahan:", e)
