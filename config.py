"""
Configuration file for Google Gemini API
"""
import os

# Google Gemini API Key
# Priority: 1) Streamlit secrets, 2) Environment variable, 3) Hardcoded fallback
try:
    # Try to import Streamlit secrets (for cloud deployment)
    import streamlit as st
    API_KEY = st.secrets.get("GOOGLE_API_KEY", None)
except:
    API_KEY = None

# Fallback to environment variable
if not API_KEY:
    API_KEY = os.getenv('GOOGLE_API_KEY')

# Fallback to hardcoded key (for local development only)
if not API_KEY:
    API_KEY = "AIzaSyDO9Zk6PZJM1B3Jx5iH8mrR2ZS3qTXG21E"

# Model configuration
MODEL_NAME = "gemini-2.5-flash-image"

# Output directory for generated images
OUTPUT_DIR = "output"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)
