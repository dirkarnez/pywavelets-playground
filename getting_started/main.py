# # -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
import pywt

def main():
  # Performing a 1D Discrete Wavelet Transform (DWT) and reconstructing the signal.
  
  # 1. Create a simple 1D signal (array of 8 numbers)
  signal = np.array([1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0])
  
  # 2. Perform Single-Level Discrete Wavelet Transform (DWT)
  # 'db1' (Daubechies 1) is the exact same as the 'haar' wavelet
  cA, cD = pywt.dwt(signal, "db1")
  
  # 3. Perform Inverse Discrete Wavelet Transform (IDWT) to reconstruct
  reconstructed_signal = pywt.idwt(cA, cD, "db1")
  
  # Print Results
  print("Original Signal:     ", signal)
  print("Approximation (cA):  ", cA)  # Low-frequency trend
  print("Detail (cD):         ", cD)  # High-frequency details (changes)
  print("Reconstructed:       ", reconstructed_signal)

if __name__ == "__main__":
  main()
