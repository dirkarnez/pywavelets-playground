# # -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
import pywt

def main():
    # 1. Create a clean signal and add random noise
    np.random.seed(42)
    clean_signal = np.sin(np.linspace(0, 10, 100))
    noise = np.random.normal(0, 0.2, 100)
    noisy_signal = clean_signal + noise

    # 2. Decompose the noisy signal into 3 levels using the Symlet 4 wavelet
    wavelet = "sym4"
    level = 3
    coefficients = pywt.wavedec(noisy_signal, wavelet, level=level)

    # 3. Calculate a noise threshold and apply it to detail coefficients
    # coefficients[0] is approximation; coefficients[1:] are details
    sigma = np.median(np.abs(coefficients[-1])) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(len(noisy_signal)))

    # Clear out noise from details (soft thresholding)
    denoised_coefficients = [coefficients[0]] + [
        pywt.threshold(c, value=threshold, mode="soft") for c in coefficients[1:]
    ]

    # 4. Reconstruct the clean signal
    denoised_signal = pywt.waverec(denoised_coefficients, wavelet)

    # Print verification
    print("Noisy Signal MSE:", np.mean((noisy_signal - clean_signal) ** 2))
    print("Denoised Signal MSE:", np.mean((denoised_signal - clean_signal) ** 2))
    
if __name__ == "__main__":
  main()
