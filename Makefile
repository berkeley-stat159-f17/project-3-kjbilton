# Create conda environment
.PHONY : env
CONDA_REQUIREMENTS=environment.yml
env : $(CONDA_REQUIREMENTS)
	conda env create -f $(CONDA_REQUIREMENTS)

.PHONY : all
NOTEBOOKS=$(wildcard *.ipynb)
NBS=$(patsubst %.ipynb, %nb, $(NOTEBOOKS))
all : $(NBS)

.PHONY : %nb
%nb: %.ipynb 
	jupyter nbconvert --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.kernel_name=python3 --to notebook --execute $< --output $< 

# Clean -- remove data
.PHONY : clean
clean :
	rm -rf results/*

# Uninstall up when done
.PHONY : uninstall
ENV_NAME=oakland
uninstall :
	conda env remove -n $(ENV_NAME) -y
