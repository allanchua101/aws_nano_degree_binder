# Creating a package for PyPi

Navigate to the `src` and run the following command:

```sh
python setup.py sdist

pip install twine
```

### Commands to upload to the PyPi test repository

```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

pip install --index-url https://test.pypi.org/simple/ pogs_dsnd
```

### Command to upload to the PyPi repository

```sh
twine upload dist/*

pip install pogs_dsnd
```
