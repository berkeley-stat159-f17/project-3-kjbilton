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

## Data Terms of Use
Air quality data (the “Data”) is provided by Google/Aclima and data analysis by Apte et al/Environmental Defense Fund, Incorporated (“EDF”). EDF owns all rights to this data. By using the Data, you (the "User") are agreeing to the Terms of Use outlined by EDF. Please read and agree to the End User Terms [here](https://www.edf.org/airqualitymaps/download-oakland-air-pollution-data). If the User decides to use the Data further in another project, all users of that project must also agree to be bound by the terms set by EDF.

## References
1. Apte, J. S.; Messier, K. P.; Gani, S.; Brauer, M.; Kirchstetter, T. W.; Lunden, M. M.; Marshall, J. D.; Portier, C. J.; Vermeulen, R. C. H.; Hamburg, S. P. High resolution air pollution mapping using Google Street View cars: exploiting big data. Environ. Sci. Technol., 2017, doi:10.1021/acs.est.7b00891.
