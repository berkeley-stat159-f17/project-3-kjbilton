# Create conda environment
# ====================================
.PHONY : env
CONDA_REQUIREMENTS=environment.yml
# Get the environment name from environment.yml
ENV=$(shell head -n 1 environment.yml | cut -f2 -d ' ')
env : $(CONDA_REQUIREMENTS)
	# Check if the environment exists
	if [[ $(conda env list | grep $(ENV)) ne 0]]; then
		echo "Conda env '$(ENV)' exists. Reinstalling now."
		# Check if you are already in the environment
		if [[ $(PATH) == *$(ENV)* ]]; then
			source deactivate
		fi
		conda env remove -n $(ENV) -y
	fi
	# Create the environment and activate
	echo "Creating conda env '$(ENV)'."
	conda env create -f $(CONDA_REQUIREMENTS)
	source activate $(ENV)

# Run all notebooks
# ====================================
.PHONY : all
NOTEBOOKS=$(wildcard *.ipynb)
NBS=$(patsubst %.ipynb, %nb, $(NOTEBOOKS))
all : $(NBS)

# Run a notebook
# ====================================
TIMEOUT=600
.PHONY : %nb
%nb: %.ipynb
	jupyter nbconvert \
		--ExecutePreprocessor.timeout=$(TIMEOUT) \
		--ExecutePreprocessor.kernel_name=python3 \
		--to notebook \
		--execute $< \
		--output $<

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
