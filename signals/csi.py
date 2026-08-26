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
