import os
from typing import Union

from napari_dataset.model import Dataset

PathLike = Union[str, os.PathLike]


def write_hdf5(path: PathLike, dataset: Dataset) -> None:
    raise NotImplementedError()  # TODO