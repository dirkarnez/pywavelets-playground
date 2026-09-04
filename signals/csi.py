import numpy as np
import numpy.typing as npt

type CSI = npt.NDArray[np.complex64]

def generate_random_wifi_csi(num_packets=100, num_subcarriers=128) -> CSI:
    """
    Generates a synthetic Wi-Fi CSI matrix containing complex values 
    representing random amplitude and phase variations per subcarrier.
    """
    # 1. Generate random amplitudes (e.g., varying between 0 and 50)
    amplitude = np.random.uniform(10, 50, size=(num_packets, num_subcarriers))
    
    # 2. Generate random phase shifts (uniformly distributed between -pi and +pi)
    phase = np.random.uniform(-np.pi, np.pi, size=(num_packets, num_subcarriers))
    
    # 3. Synthesize the complex CSI matrix: H = A * e^(j * phase)
    return amplitude * np.exp(1j * phase)


""""
import numpy as np
import matplotlib.pyplot as plt
import pywt

# 1. Simulate a WiFi CIR Signal (3 Multipath Path Taps + Noise)
num_taps = 64
cir_clean = np.zeros(num_taps)
cir_clean[8] = 1.2   # Direct Line-of-Sight (LoS) path
cir_clean[18] = 0.6  # Reflection path 1
cir_clean[32] = 0.3  # Reflection path 2

# Add typical high-frequency phase and hardware noise
noise = np.random.normal(0, 0.15, num_taps)
cir_noisy = cir_clean + noise

# 2. Decompose using PyWavelets ('sym4' or 'db4' work well for radio paths)
wavelet = 'sym4'
mode = 'per' # Periodic boundary handling
cA, cD = pywt.dwt(cir_noisy, wavelet, mode=mode)

# 3. Soft-Threshold the high-frequency detail coefficients to kill noise
# Calculate universal threshold (Donohio-Johnstone method)
sigma = np.median(np.abs(cD)) / 0.6745
threshold = sigma * np.sqrt(2 * np.log(len(cir_noisy)))
cD_filtered = pywt.threshold(cD, value=threshold, mode='soft')

# 4. Reconstruct the clean CIR signal using Inverse DWT
cir_denoised = pywt.idwt(cA, cD_filtered, wavelet, mode=mode)

# 5. Plot the WiFi CIR results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(cir_noisy, linefmt='r-', markerfmt='ro', basefmt='k-', label='Noisy Raw CIR')
plt.title("Raw WiFi Channel Impulse Response (With Noise)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(cir_denoised[:num_taps], linefmt='b-', markerfmt='bo', basefmt='k-', label='Denoised CIR')
plt.title("Cleaned WiFi Channel Impulse Response (After Wavelet Denoising)")
plt.xlabel("Delay Taps (Time Domain)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

""""

"""
import numpy as np
import matplotlib.pyplot as plt
import pywt

# 1. Generate a sample signal (Sine wave + random noise)
t = np.linspace(0, 1, 400)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(400)

# 2. Perform Single Level Discrete Wavelet Transform
# Using 'db4' (Daubechies 4) for smoother decomposition
cA, cD = pywt.dwt(signal, 'db4')

# 3. Plotting the results
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=False)

# Original Signal Plot
axes[0].plot(signal, color='black', alpha=0.7)
axes[0].set_title('Original Noisy Signal')
axes[0].grid(True)

# Approximation (Low-frequency trend)
axes[1].plot(cA, color='blue')
axes[1].set_title('Approximation Coefficients (cA) - Low Frequency / Trend')
axes[1].grid(True)

# Details (High-frequency noise/sharp changes)
axes[2].plot(cD, color='red')
axes[2].set_title('Detail Coefficients (cD) - High Frequency / Noise')
axes[2].grid(True)

plt.tight_layout()
plt.show()

"""
