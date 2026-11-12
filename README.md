# UV-Vis Data Analysis & Tauc Plot (Python)

This Python script is designed to analyze UV-Vis spectroscopy data, extract optical properties, and calculate the optical band gap of semiconductor materials using the Tauc Plot method.

## 📊 What This Script Does (Data Analysis)

The script takes raw UV-Vis data (Wavelength, Transmittance, Absorbance) and performs the following steps:

1. **Data Extraction:** Reads `.xlsx` or `.csv` files.
2. **Absorption Coefficient (\(\alpha\)):** Calculates the absorption coefficient using the formula:
   \(\alpha = \frac{2.303 \times A}{d}\) (where \(A\) is Absorbance and \(d\) is the sample thickness).
3. **Photon Energy (\(E\)):** Converts wavelength (nm) to photon energy (eV) using \(E = \frac{hc}{\lambda}\).
4. **Tauc Plot Generation:** For direct band gap semiconductors, it plots \((\alpha h\nu)^2\) versus \(h\nu\).
5. **Band Gap Calculation:** Fits a linear curve to the linear region of the Tauc plot and extrapolates it to the x-axis to estimate the optical band gap (\(E_g\)).

## 📈 Output
The script generates a high-quality 3-panel figure (saved as `uvvis_analysis.png`):
- **Left:** Optical Transmittance (%) vs. Wavelength.
- **Middle:** UV-Vis Absorbance (a.u.) vs. Wavelength.
- **Right:** Tauc Plot with the linear fit and calculated Band Gap (\(E_g\)
