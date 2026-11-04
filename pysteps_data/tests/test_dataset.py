import pathlib

from pysteps_data import DATASETS, locate


def test_registry():
    files = DATASETS.registry_files
    assert len(files) > 0


def test_locate():
    p = locate()
    assert 'pysteps-data' in p
    assert pathlib.Path(p).exists
