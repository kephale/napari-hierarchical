try:
    from napari_hierarchical._version import version as __version__
except ImportError:
    __version__ = "unknown"

from napari_hierarchical._controller import (
    HierarchicalController,
    HierarchicalControllerException,
    controller,
)
from napari_hierarchical._reader import napari_get_reader
from napari_hierarchical.contrib import hdf5, imc, zarr

if hdf5.available:
    controller.pm.register(hdf5, name="napari-hierarchical-hdf5")
if imc.available:
    controller.pm.register(imc, name="napari-hierarchical-imc")
if zarr.available:
    controller.pm.register(zarr, name="napari-hierarchical-zarr")

__all__ = [
    "controller",
    "HierarchicalController",
    "HierarchicalControllerException",
    "napari_get_reader",
]
