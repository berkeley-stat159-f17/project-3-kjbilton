# Create conda environment
# ====================================
.PHONY : env
CONDA_REQUIREMENTS=environment.yml
# Get the environment name from environment.yml
ENV=$(shell head -n 1 $(CONDA_REQUIREMENTS) | cut -f2 -d ' ')
env : $(CONDA_REQUIREMENTS)
	@echo "Creating conda env '$(ENV)'."
	conda env create -f $(CONDA_REQUIREMENTS)

# Run all notebooks
# ====================================
.PHONY : all
NOTEBOOKDIR=notebooks/
NOTEBOOKS=$(wildcard $(NOTEBOOKDIR)*.ipynb)
NBS=$(patsubst $(NOTEBOOKDIR)%.ipynb, %nb, $(NOTEBOOKS))
all : $(NBS)

# Run a notebook
# ====================================
TIMEOUT=600
.PHONY : %nb
%nb: $(NOTEBOOKDIR)%.ipynb
	jupyter nbconvert \
		--ExecutePreprocessor.timeout=$(TIMEOUT) \
		--ExecutePreprocessor.kernel_name=python3 \
		--to notebook \
		--execute $< \
		--output $(patsubst $(NOTEBOOKDIR)%.ipynb, %.ipynb, $<)

# Clean: remove intermediate results
# ====================================
.PHONY : clean
clean :
	rm -rf results/*

# Uninstall the conda environment
# ====================================
.PHONY : uninstall
uninstall :
	conda env remove -n $(ENV) -y
