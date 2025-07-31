import pickle
import numpy as np
import pandas as pd  # import pandas

# Load model
model = pickle.load(open('../models/house_price_model.pkl', 'rb'))

def predict_price(features: list):
    """
    Predict house price.
    Args:
        features (list): List of input features in order
            ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
    Returns:
        float: predicted price
    """
    feature_names = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
    
    # Create DataFrame with column names
    final_features = pd.DataFrame([features], columns=feature_names)
    
    prediction = model.predict(final_features)
    return round(prediction[0], 2)
