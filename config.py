from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
