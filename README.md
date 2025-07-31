# House Price Prediction

A machine learning project to predict house prices using Random Forest regression and deploy it as an interactive Streamlit web app.

## Project Overview

This project uses a housing dataset containing various features like overall quality, living area, garage capacity, basement size, bathrooms, and year built to predict house sale prices.

## Features

- Data preprocessing and exploratory data analysis (EDA)  
- Machine learning model training using Random Forest Regressor  
- Model evaluation using R² score  
- Model serialization with pickle  
- Interactive web app built with Streamlit for real-time price prediction

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   
2.Install dependencies:

pip install -r requirements.txt

3.Usage(Optional) Train the model (if you want to retrain with your data):

python train_model.py

4.Run the Streamlit app:

streamlit run app/app.py

5.Open your browser at http://localhost:8501 and use the app to predict house prices by entering feature values.

## Sample Input Features

1.OverallQual: Overall quality of the house (1-10)

2.GrLivArea: Above ground living area in square feet

3.GarageCars: Number of cars that fit in garage

4.TotalBsmtSF: Total basement area in square feet

5.FullBath: Number of full bathrooms

6.YearBuilt: Year the house was built

## Project Structure

house-price-prediction/
│
├── app/                  # Streamlit app files
│   ├── app.py
│   └── predictor.py
│
├── data/                 # Dataset files
│   └── housing.csv
│
├── models/               # Trained model files
│   └── house_price_model.pkl
│
├── notebooks/            # Jupyter notebooks for EDA and model training
│   └── EDA_and_Model.ipynb
│
├── train_model.py        # Script to train and save the model
├── requirements.txt      # Project dependencies
└── README.md             # This file

## Technologies Used

1.Python

2.Pandas, NumPy

3.Scikit-learn

4.Streamlit

5.Matplotlib, Seaborn

## Author
FAREEDA BEGUM SHEIK

## requirements.txt

1.pandas

2.numpy

3.scikit-learn

4.streamlit

5.matplotlib

6.seaborn

