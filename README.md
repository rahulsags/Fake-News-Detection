# Fake-News-Detection

## Introduction

This project aims to detect fake news based on the content provided by users. It uses natural language processing (NLP) techniques and machine learning algorithms to classify news headlines. The web application allows users to enter text and predict whether the news is **reliable** or **unreliable**.

## Technologies Used

- **Python**: Programming language
- **Streamlit**: Web application framework
- **scikit-learn**: Machine learning library for model training
- **nltk**: Natural Language Toolkit for text processing
- **pickle**: For saving and loading models
- **Pandas**: For data manipulation
- **NumPy**: For numerical operations

## Features

- Enter news content through a simple interface.
- Get a prediction on whether the news is **reliable** or **unreliable**.
- Uses a pre-trained **Decision Tree Classifier** model to predict news reliability.

## Setup and Installation

To set up and run the application locally, follow these steps:

1. Clone this repository
2. Navigate into the project directory
3. Create a **virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
   - **On Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. Install the required libraries:
    ```bash
    pip install -r req.txt
    ```

## Usage

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
