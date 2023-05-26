"""Top-level package for dolfin_pyvista_adapter."""
from importlib.metadata import metadata
from .source import create_vtk_structures, plot


meta = metadata("dolfin_pyvista_adapter")
__version__ = meta["Version"]
__author__ = meta["Author"]
__license__ = meta["License"]
__email__ = meta["Author-email"]
__program_name__ = meta["Name"]

__all__ = ["create_vtk_structures", "plot"]
