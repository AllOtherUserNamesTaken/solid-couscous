# How To Install

### Dependency on Python >=3.8

## 1. Use Build Artefact

Download the zipped build artefact (under the actions tab if available), unzip and then execute pip install using the wheel (*.whl file).

## 2. Use Poetry

Clone the repository, ensure python poetry is installed and ensure that you can create a python 3.8 environment. Execute `poetry install` then `poetry shell` to have an activated environment.

# How To Use

In general execute `python -m solid_couscous.app ${PATH_TO_FILE}` or use `python -m solid_couscous.app -` for stdin. For help use `python -m solid_couscous.app --help`. 