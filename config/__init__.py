
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# AI model configuration
MODEL_NAME = "gemini-2.5-flash"

# Student dataset path
DATA_FILE = "data/students.csv"

# Risk level thresholds
HIGH_RISK_THRESHOLD = 60
MEDIUM_RISK_THRESHOLD = 35
