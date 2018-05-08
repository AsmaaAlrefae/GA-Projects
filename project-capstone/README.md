# About



# File Structure

```
├── LICENSE
├── README.md           <- This.
├── data
│   ├── processed       <- The final, canonical data sets for modeling.
│   ├── raw             <- The original, immutable data dump.
│   └── make_dataset.md <- Script to upload to Neo4j database
│
├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references          <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── assets          <- Generated graphics and figures to be used in reporting
│
├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── src                 <- Source code the Flask web app
    ├── __init__.py     <- 
    │
    ├── app.py          <- Main script for the Flask app
    │
    ├── models.py       <- Where all the functions for the Flask are found
    │
    └── templates       <- CSS, HTML, etc.
        ├── index.html
        └── display.html
```