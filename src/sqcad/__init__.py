# src/sqcad/__init__.py

"""sqCAD: superconducting quantum circuit analysis & design."""

from __future__ import annotations

import os


__version__ = "0.1.0"
__license__ = "MIT License"
__copyright__ = "Elizabeth Kunz, Eli Levenson-Falk 2026"
__author__ = "Elizabeth Kunz"
__status__ = "Alpha"

__package_path__ = os.path.dirname(os.path.abspath(__file__))


from sqcad.elements import resonators
from sqcad import models, utils

__all__ = [
    "resonators",
    "models",
    "utils",
    "__version__",
    "__license__",
    "__copyright__",
    "__author__",
    "__status__",
    "__repo_path__",
]


# from __future__ import annotations

# __all__ = ["__version__", "about"]


# def about() -> str:
#     return "sqCAD (Superconducting Quantum Circuit Analysis & Design)"