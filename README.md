# MeliExercise

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Data science project to predict whether a listed item is new or used

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── Documentacion      <- A default mkdocs project; see www.mkdocs.org for details
│   MeliExercise
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         meliexercise and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── meliexercise   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes meliexercise a Python module
    │
    ├── classes                 <- Contains the pipeline classes
    │   ├── __init__.py         <- Makes classes a Python module 
    │   ├── data_loader.py      <- Class to load the data          
    │   ├── data_cleaner.py     <- Class to clean the data    
    │   ├── feature_engineer.py <- Class to do feature engineer to the data        
    │   ├── feature_selector.py <- Class to do feature selection to the data     
    │   ├── model_trainer.py    <- Class to train the model         
    │   └── train.py            <- Code to train models  
    │

    └── plots.py                <- Code to create visualizations
```

--------

