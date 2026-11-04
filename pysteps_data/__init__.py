#!/usr/bin/env python3
"""Top-level module for pysteps-data."""
from importlib.metadata import version as _version

from .dataset import DATASETS, locate

try:
    __version__ = _version(__name__)
except Exception:  # pragma: no cover
    # package is not installed
    __version__ = 'unknown'  # pragma: no cove
