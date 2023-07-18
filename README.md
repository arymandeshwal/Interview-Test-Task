# Fact-Checking-Engine
[Project Overview](#project-overview)  | [Installation](#installation)   | [Techniques](#techniques) | [Contribution](#contribution)

## Project Overview
Fact checker - A Fact Checking Engine  based on Wikipedia corpus , developed using Ensemble models approach.

This project aims to validate the veracity of a given triple (s, p, o) using a knowledge graph G and a maximum path length k. It begins by initializing the necessary variables and performing path discovery. Paths are discovered by generating query templates and executing queries to obtain relevant information.  Finally, the veracity of the triple is calculated based on the prediction of models. The algorithm returns a veracity score [0,1] for the input triple.

## Installation

- pip install -r requirements.txt
- You will need Jupyter Notebook
- Just Run the file main.ipynb

## Techniques
Ensemble model
An algorithm that aims to validate facts by utilizing information from a knowledge graph and using RandomForest, LogisticRegression and KNN to predict.

## Contribution:

| Name                  | Matriculation Number |
| --------------------- | -------------------- |
| Amal Nimmy Lal   |   6987112            |
| Aryman Deshwal   |  4011205           |
