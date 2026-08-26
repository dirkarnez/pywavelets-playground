import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes


class MatplotlibHelper:
    nrows: int
    ncols: int
    index: int
    fig: Figure
    axs: Axes
    file_name: str

    def __init__(self, nrows: int, ncols: int, file_name: str):
        if nrows * ncols < 2:
            raise Exception("At least 2")
        self.nrows = nrows
        self.ncols = ncols
        self.file_name = file_name
        self.index = 0

    def __enter__(self):
        self.fig, self.axs = plt.subplots(self.nrows, self.ncols)
        return self

    def add(self, data: npt.ArrayLike):
        self.axs[self.index].plot(data)
        print(f"index: {self.index}")
        self.index += 1
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        plt.tight_layout()
        plt.savefig(self.file_name)
        plt.clf()
