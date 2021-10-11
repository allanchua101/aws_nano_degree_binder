# Creating Python Package

This folder is used for showcasing how can a local package be installed using `pip`.

### Navigate to this folder and run

```sh
pip3 install matplotlib

# Make sure that you are at the current directory.
pip3 install . --user
```

### Testing the local package installation

```py
from distributions import Gaussian

gaussian_one = Gaussian(25, 2)

gaussian_one.mean

gaussian_one + gaussian_one
```
