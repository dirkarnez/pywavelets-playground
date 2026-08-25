pywavelets-playground
=====================
Performing a 1D Discrete Wavelet Transform (DWT) and reconstructing the signal.

## Notes
* `pywt.dwt()`: Splits your data into two parts.
* `cA` (Approximation): The "blurry" or averaged version of your data (low frequencies).
* `cD` (Detail): The sharp changes, noise, or edges (high frequencies).
* Wavelet Name: `"db1"` (or "haar") is the simplest wavelet available and is perfect for beginners.
