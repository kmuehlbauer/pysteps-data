# pysteps data
pysteps example data 

This repository contains example data used by the pysteps example scripts.

## Adding new datasets

To add a new dataset file, please follow these steps:

1. Add the dataset file to the `data/` directory
2. From the command line, run `python make_registry.py` script to update the registry file residing in `pysteps_data/registry.txt`
3. Commit and push your changes to GitHub

## Using datasets in examples and/or scripts

- Ensure the `pysteps_data` package is installed in your environment

```bash
python -m pip install git+https://github.com/PYSTEPS/pysteps-data
```

- Import `DATASETS` and inspect the registry to find out which datasets are available

  ```python
  In [1]: from pysteps_data import DATASETS

  In [2]: DATASETS.registry_files
  Out[2]: ['radar/KNMI/2010/08/RAD_NL25_RAP_5min_201008260015.h5`]
  ```

- To fetch a data file of interest, use the `.fetch` method and provide the filename of the data file. This will

  - download and cache the file if it doesn't exist already.
  - retrieve and return the local path

  ```python
  In [4]: filepath = DATASETS.fetch('radar/KNMI/2010/08/RAD_NL25_RAP_5min_201008260015.h5')

  In [5]: filepath
  Out[5]: '/home/kai/.cache/pysteps-data/radar/KNMI/2010/08/RAD_NL25_RAP_5min_201008260015.h5'
  ```

## Changing the default data cache location

The default cache location (where the data are saved on your local system) is dependent on the operating system. You can use the `locate()` method to identify it:

```python
from pysteps_data import locate
locate()
```

The location can be overwritten by the `PYSTEPS_DATASET_DIR` environment
variable to the desired destination.


# Data disclaimers

## RMI data

This example data originating from RMI (Royal Meteorological Institute of
Belgium)  may not be used for commercial purposes, all property and
intellectual rights are an exclusivity of the RMI and may not be transferred,
the source of the data must be cited in each publication in which the data of
the RMI have been used.


