# 🛍️ MeliExercise

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Data science project to predict whether a listed item is new or used

## 📚 Model Documentation

[Documentation](https://YarlyMadrid.github.io/MeliExercise)

## 🗂️ Project Organization

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
## 🔖 Commit Conventions

Este es una convención que utiliza prefijos específicos en los mensajes de commit para indicar el tipo de cambio que se realizó en el código.

**Recomendaciones:**

* Usar el mismo idioma dentro del mismo repositorio para mayor coherencia y claridad, se recomienda inglés por universalidad.

* Escribir los commits iniciando con verbos en presente simple, es decir, crear, actualizar, administrar o *create, update, manage* en inglés.

* Cuando se va a realizar un cambio que podría ser muy grande o "rompedor", usar el formato **BREAKING CHANGE** en el que si se va a realizar un gran cambio, se deja un ! luego del prefijo y el alcance/contexto, ejemplo:  	```
fix(lambda)!: Change of the orchestration to step functions.	```

<table>
  <tr>
    <th colspan="4" align="center">🚀CONVENTIONAL COMMIT🚀</th>
  </tr>
  
  <tr>
    <th align="center"><strong>Tipo (prefijo)</strong></th>
    <th align="center"><strong>Contexto</strong></th>
    <th align="center"><strong>Descripción</strong></th>
    <th align="center"><strong>Ejemplo</strong></th>
  </tr>
  <tr>
    <td align="center">feat</td>
    <td align="center">classes</td>
    <td>Añadir clase para limpieza de datos</td>
    <td><code>feat (classes): Add functions to clean data</code></td>
  </tr>
  <tr>
    <td align="center">fix</td>
    <td align="center">data</td>
    <td>Corregir repositorio de datos actualizado</td>
    <td><code>fix (data): Fix the clients data repository</code></td>
  </tr>
  <tr>
    <td align="center">docs</td>
    <td align="center">docs</td>
    <td>Crear la documentación inicial del proyecto</td>
    <td><code>docs (docs): Create README.md file of the project</code></td>
  </tr>
  <tr>
    <td align="center">chore</td>
    <td align="center">Models</td>
    <td>Adicionar nueva variable “edad” al modelo</td>
    <td><code>chore (models): Add new variable age, to the model</code></td>
  </tr>
  <tr>
    <td align="center">test</td>
    <td align="center">notebooks</td>
    <td>Pruebas sobre el resultado del notebook generado</td>
    <td><code>test (notebooks): Create unit test of a notebook component</code></td>
  </tr>
  <tr>
    <td colspan="4"  align="center"><strong>Source:</strong> <a href="https://www.conventionalcommits.org/en/v1.0.0/">https://www.conventionalcommits.org/en/v1.0.0/</a></td>    
  </tr>
  <tr>    
    <td colspan="4" align="center"><strong>Created by:</strong> Yarly Madrid</td>
  </tr>
</table>


## 💻 Tech Stack

**Programming Language:** Python 🐍

**Principal Libraries Used** 

* xgboost==3.0.0 
* lightgbm==4.6.0 
* numpy==2.2.4 
* pandas==2.2.3 
* scikit-learn==1.6.1 
* xgboost==3.0.0

For more details go to *requirements.txt*.

## 🚀 Run Locally

Clone the project

```bash
  git clone https://github.com/YarlyMadrid/MeliExercise
```

Go to the project directory

```bash
  cd MeliExercise
```
Activate the environment
```bash
  .\.venv\Scripts\activate
```
Install python libraries in the virtual enviroment

```bash
  pip install -r .\requirements.txt
```

To train the model execute the file "new_or_used.py"

```bash
  python -m meliexcercise.new_or_used
```

--------

