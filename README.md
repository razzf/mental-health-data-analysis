# Data Analysis of the Mental Health in the Tech Industry Course Dataset

## Overview

This repository contains a brief analysis of the *Mental Health in the Tech Industry* dataset, which investigates the mental health challenges faced by professionals in the technology sector. The dataset consists of responses from multiple surveys conducted over several years, addressing various aspects of mental health, including diagnoses, treatment experiences, and workplace support systems. 

## Objectives

The primary objectives of this analysis are to:
- Examine the prevalence of mental health disorders among tech industry employees.
- Identify demographic differences, particularly concerning gender and age, in mental health experiences.
- Highlight biases in the survey data and discuss their implications for generalizability.

## Table of Contents 

- 1. [Introduction](#introduction)    
- 2. [Data preparation](#data-preparation)    
- 3. [Data cleaning](#data-cleaning)      
- 4. [Exploratory data analysis (EDA)](#exploratory-data-analysis-eda)    
  - 4.1. [Respondent overview](#respondent-overview)    
  - 4.2. [Sample size](#sample-size)    
  - 4.3. [Age](#age)    
  - 4.4. [Gender](#gender)    
  - 4.5. [Country of residence](#country-of-residence)    
  - 4.6. [Self-employment](#self-employment)    
- 5. [Feature analysis on Mental Health Disorders](#feature-analysis-on-mental-health-disorders)    
  - 5.1. [Family history of mental illness](#family-history-of-mental-illness)    
  - 5.2. [Professional treatment for a mental health disorder](#professional-treatment-for-a-mental-health-disorder)    
  - 5.3. [Mental health disorder in the past](#mental-health-disorder-in-the-past)    
  - 5.4. [Current mental health disorder](#current-mental-health-disorder)    
  - 5.5. [Diagnosed mental health disorder](#diagnosed-mental-health-disorder)    
  - 5.6. [Mental health disorder: A first summary](#mental-health-disorder-a-first-summary)    
- 6. [Analysis of the prevalence rate of mental diseases](#analysis-of-the-prevalence-rate-of-mental-diseases)    
  - 6.1. [Prevalence rate of mental diseases](#prevalence-rate-of-mental-diseases)    
  - 6.2. [Gender differences in the prevalence rates of mental diseases](#gender-differences-in-the-prevalence-rates-of-mental-diseases)    
- 7. [Suggestions for further research](#suggestions-for-further-research)    
- 8. [Summary](#summary)    

## Contents

- **`data_analysis_mental_health.ipynb`**: The main Jupyter notebook containing the data preparation, analysis, and visualizations.
- **`data/`**: Directory containing the raw dataset used for analysis.
- **`requirements.txt`**: List of Python dependencies required to run the Jupyter notebook.

## Project Structure

1. **Introduction**: Overview of the dataset and the aims of the project.
2. **Data preparation**: Detailed steps regarding the source, design, sampling, and documentation of the dataset.
3. **Data cleaning**: Detailed steps for preparing the data for analysis.
4. **Exploratory data analysis (EDA)**: Analyzes and visualizes the data to gain first insights.
5. **Feature analysis on Mental Health Disorders**: Investigates various features on mental health disorders and their treatment.
6. **Analysis of the prevalence rate of mental diseases**: Investigates the rates of various mental health disorders and gender differences.
7. **Suggestions for further research**: Proposes areas for additional investigation in the field of mental health.
8. **Summary**: Key findings, limitations, and conclusions drawn from the analysis.
 
## Key Findings

- **Increasing Mental Health Disorders Diagnoses**: The analysis reveals a significant upward trend in reported mental health diagnoses over the years, indicating a growing awareness and acknowledgment of mental health issues in the tech industry.

- **Gender Differences in Mental Health**: Women reported higher rates of mood and anxiety disorders compared to their male counterparts, underscoring the necessity for gender-sensitive mental health support and interventions in the workplace.

## Installation and Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mental-health-in-tech.git
   cd mental-health-in-tech

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Launch the Jupyter notebook to explore the analysis:
   ```bash
    jupyter notebook data_analysis_mental_health.ipynb

## Custom Modules

This project includes custom Python modules located in the `custom_modules` directory. These modules contain reusable functions and utilities used throughout the analysis. Ensure you download this directory when cloning the repository.

You can import these modules into your notebook or scripts as follows:

```python
from custom_modules import module_name
```

Replace `module_name` with the specific module you want to use.

## Data

The dataset used in this analysis is available in the `data` subdirectory. It includes the necessary Database file (mental_health.sqlite) for running the analysis. Ensure that this directory is in the project root, as the notebook depends on relative paths to load the data. Originally the dataset was sourced from [Kaggle](https://www.kaggle.com/anth7310/mental-health-in-the-tech-industry). Throughout this project a working copy of the Database file will be created, to ensure that the original remains as a backup.
 