# -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
from utils.plotting import MatplotlibHelper
from denoising.main import demo_1
from signals.csi import CSI, generate_random_wifi_csi

def main():
    csi_data: CSI  = generate_random_wifi_csi(100, 128)

    # print(f'{helper} with statement block')
    demo_1_tuple = demo_1()
    (original, polluted, denoised) = demo_1_tuple

    with MatplotlibHelper(len(demo_1_tuple), 1, "denoising_demo_1.png") as helper:
       helper.add(original)
       helper.add(polluted)
       helper.add(denoised)

    with MatplotlibHelper(2, 1, "csi.png") as helper:
       helper.add(np.abs(csi_data[0]))
       helper.add(np.abs(csi_data[1]))

if __name__ == "__main__":
    main()
