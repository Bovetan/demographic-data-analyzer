# Demographic Data Analyzer

This project is part of the FreeCodeCamp Data Analysis with Python certification.

## Description

This Python project uses the Pandas library to analyze demographic data from the `adult.data.csv` dataset.

The program answers the following questions required by FreeCodeCamp:

1. How many people of each race are represented in the dataset?
2. What is the average age of men?
3. What percentage of people have a Bachelor's degree?
4. What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
8. Which country has the highest percentage of people that earn more than 50K?
9. What is the most popular occupation for those who earn more than 50K in India?

## Technologies Used

- Python
- Pandas

## Project Files

- `demographic_data_analyzer.py` → main solution file
- `adult.data.csv` → dataset used for the analysis / The dataset (adult.data.csv) is included in this repository.
- `main.py` → optional file for local testing

## How to Use

1. Clone the repository:

git clone https://github.com/Bovetan/demographic-data-analyzer

2. Navigate to the project folder:

cd demographic-data-analyzer

3. Run the program:

python main.py

## Example

The function returns a dictionary with the calculated results:

```python
from demographic_data_analyzer import calculate_demographic_data

print(calculate_demographic_data())
