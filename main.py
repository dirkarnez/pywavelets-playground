# -*- coding: utf-8 -*-
from typing import Any, List

import numpy as np
from utils.plotting import MatplotlibHelper
from denoising.main import demo_1

def main():
    # print(f'{helper} with statement block')
    demo_1_tuple = demo_1()
    (original, polluted, denoised) = demo_1_tuple
    
    with MatplotlibHelper(len(demo_1_tuple), 1, "denoising_demo_1.png") as helper:
       helper.add(original)
       helper.add(polluted)
       helper.add(denoised)

    # with MatplotlibHelper(2, 1, "rt.png") as helper:
    #    helper.add(np.array([1, 2, 3]))
    #    helper.add(np.array([1, 2, 3]))

if __name__ == "__main__":
    main()
