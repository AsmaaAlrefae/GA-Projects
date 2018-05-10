# Context

Capstone project for General Assembly's Data Science Immersive Course in Singapore (Batch 03). From Feb 2018 to May 2018.

# About the Project

A recipe recommender system using Instacart's 2017 sales data and Epicurious's recipes. Powered by Neo4j and Python. Served as a Flask web app. Hosted on [tbd].

# File Structure

```
├── LICENSE
├── README.md           <- This.
├── data
│   ├── processed       <- The final, canonical data sets for modeling.
│   ├── raw             <- The original, immutable data dump.
│   └── make_dataset.md <- Script to upload to Neo4j database.
│
├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering), 
│                          and a short `-` delimited description. xx denotes old notebooks, with broken internal links.
│
├── references          <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── assets          <- Generated graphics and figures to be used in reporting and in jupyter notebooks.
│
├── requirements.txt    <- The requirements file for reproducing the analysis environment.
│
└── src                 <- Source code for the Flask web app.
    ├── __init__.py     <- A Flask/Python thing.
    │
    ├── app.py          <- Main script for the Flask app.
    │
    ├── models.py       <- Where all the functions for the Flask are found.
    └── templates       <- HTML.
        ├── index.html  <- Landing page "/".
        ├── layout.html <- Base layout.
        ├── recipes.html<- Content block for recipes page.
        └── display.html<- Content block for "feeling_hungry".
```