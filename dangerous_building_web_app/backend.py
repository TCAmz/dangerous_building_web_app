import streamlit as st
import pandas as pd

def create_df(file):
    df = pd.read_csv(file)
    return df

