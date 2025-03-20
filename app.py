from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
import pandas as pd
import os
from pymongo import DESCENDING, ASCENDING
from config import Config
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure MongoDB
app.config.from_object(Config)
mongo = PyMongo(app)

# Ensure the upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_csv():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Clear existing data to prevent duplication
    mongo.db.movies.delete_many({})

    # Process CSV in chunks to handle large files
    chunk_size = 10000  # Process 10,000 rows at a time
    for chunk in pd.read_csv(filepath, dtype=str, chunksize=chunk_size):
        chunk.fillna("", inplace=True)  # Replace NaN with empty strings

        # Convert relevant fields
        if "release_date" in chunk.columns:
            chunk["release_date"] = pd.to_datetime(chunk["release_date"], errors="coerce")
            chunk["release_date"] = chunk["release_date"].dt.strftime("%Y-%m-%d").fillna("N/A")  

        if "year" in chunk.columns:
            chunk["year"] = chunk["year"].astype(str)

        if "languages" in chunk.columns:
            chunk["languages"] = chunk["languages"].apply(lambda x: x.split(",") if isinstance(x, str) else [])

        # Convert to list of dictionaries and insert into MongoDB
        movies_list = chunk.to_dict(orient="records")
        if movies_list:
            mongo.db.movies.insert_many(movies_list)

    return jsonify({"message": "File uploaded successfully."}), 200

@app.route("/movies", methods=["GET"])
def get_movies():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    year = request.args.get("year")  
    language = request.args.get("language")
    sort_by = request.args.get("sort_by", "release_date")
    order = request.args.get("order", "asc").lower()

    sort_order = ASCENDING if order == "asc" else DESCENDING

    query = {}

    if year:
        query["release_date"] = {"$regex": f"^{year}"}

    if language:
        query["languages"] = {"$regex": language, "$options": "i"}

    movies = list(
        mongo.db.movies.find(query)
        .sort(sort_by, sort_order)
        .skip((page - 1) * limit)
        .limit(limit)
    )

    return render_template("view.html", movies=movies, page=page, limit=limit, request=request)

if __name__ == "__main__":
    app.run(debug=True)
