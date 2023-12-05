import logging
import pandas as pd
from zenml import step

@step
def clean_data(df:pd.DataFrame)->pd.DataFrame:
    """Clean the data by removing duplicates and missing values"""
    pass