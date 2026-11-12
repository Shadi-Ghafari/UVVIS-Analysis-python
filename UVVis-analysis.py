import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel(r"D:\python project\uvvis_data.excel.xltx")
print("shape:", df.shape)
print(df.head())
w1 = df.iloc[:, 0].values
T = df.iloc[:, 1].values
A = df.iloc[:, 2].values
d = 5e-5
alpha = 20303 * A / d
h = 4.13566667696e-15
c = 3e8
E = h * c / (w1 * 1e-9)
y = (alpha * E)**2
y_norm = y / np.max(y)
mask = (E > 2.0) & (E < 2.5)
coeffs = np.polyfit(E[mask], y_norm[mask], 1)
Eg = -coeffs[1] / coeffs[0]
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
axes[0].plot(w1, T*100, 'g-', linewidth=1.5)
axes[0].set_xlabel('wavelength (nm)')
axes[0].set_ylabel('Transmittance (%)')
axes[0].set_title('Optical Transmittance')
axes[0].grid(alpha=0.3)
axes[1].plot(w1, A, 'b', linewidth=1.5)
axes[1].set_xlabel('wavelength (nm)')
axes[1].set_ylabel('Absorbance (a.u.)')
axes[1].set_title('UV_Vis Absorption')
axes[1].grid(alpha=0.3)
axes[2].plot(E, y_norm, 'k-', linewidth=1.5, label='Data')
axes[2].plot(E[mask], np.polyval(coeffs, E[mask]), 'r--', linewidth=1.5, label=f'Linear fit, Eg = {Eg: 2f} ev')
axes[2].set_xlabel('Photon Energy (ev)')
axes[2].set_ylabel('((αhν)^2, normalized)')
axes[2].set_title('Tauc plot, fontsize=12')
axes[2].legend()
axes[2].grid(alpha=0.3)
axes[2].set_xlim(1.5, 4.0)
plt.tight_layout()
plt.savefig('uvvis_analysis.png', dpi=300, bbox_inches='tight')
plt.show()