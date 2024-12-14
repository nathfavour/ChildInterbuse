# Child Mind Institute — Problematic Internet Use

## Overview
This project aims to predict the level of problematic internet usage exhibited by children and adolescents based on their physical activity. The goal is to develop a predictive model that analyzes children's physical activity and fitness data to identify early signs of problematic internet use.

## Directory Structure
```
ChildInterbuse/
│
├── data/
│   ├── raw/                # Raw data files
│   ├── processed/          # Processed data files
│
├── notebooks/              # Jupyter notebooks
│
├── src/                    # Source code
│   ├── data/               # Data loading and preprocessing scripts
│   ├── models/             # Model definition and training scripts
│   ├── utils/              # Utility functions
│
├── models/                 # Trained models
│
├── requirements.txt        # Dependencies
├── .gitignore              # Git ignore file
└── README.md               # Project overview
```

## Getting Started
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd ChildInterbuse
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the dataset and place it in the `data/raw/` directory.

4. Run the Jupyter notebooks in the `notebooks/` directory to explore and preprocess the data, train models, and make predictions.

## Acknowledgments
The data used for this competition was provided by the Healthy Brain Network, a landmark mental health study based in New York City.
