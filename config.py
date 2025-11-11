"""
Configuration file for Google Gemini API
"""
import os

# Google Gemini API Key
# For security, consider using environment variables in production
API_KEY = "AIzaSyDO9Zk6PZJM1B3Jx5iH8mrR2ZS3qTXG21E"

# Alternative: Load from environment variable
# API_KEY = os.getenv('GOOGLE_API_KEY', 'your-api-key-here')

# Model configuration
MODEL_NAME = "gemini-2.5-flash-image"

# Output directory for generated images
OUTPUT_DIR = "output"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)
