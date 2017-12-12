# Quantifying Gentrification through Contextual Information

## Overview
In this project, I explore potential methods of quantifying gentrification through the use of contextual clues and non-economic data (e.g., reports of graffiti). In particular, I explore these methods in the city of Oakland, California, where the nearby technology industry has introduced a wave of high earners in the West side of the city.

An analysis is presented in the form of Jupyter notebooks, using standard Python data science and geospatial analysis tools to generate results. The structure of the repository is:

- main.ipynb
    - A summary of results and methods used.
- notebooks
    - A directory containing sequential Jupyter notebooks for reproducing the analyses.
- fig
    - A directory containing figures generated in the analysis.

## Usage
### Environment
You must first have conda installed before the environment can be built. To install the environment, run

```
make env
```

This command will create a conda environment named `oakland` with all Python packages required to run the analyses.

### Running the analyses
All code can be ran and figures saved by running
```
make all
```
Alternatively, one can run all notebooks individually and explore intermediate results along the way.

### Testing
Modules can be tested from the top-level directory with the command
```
pytest
```
This runs all tests within the `test` directory.
