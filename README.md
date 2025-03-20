# Movie Data Upload & Retrieval API

An advanced Flask-based web application that allows users to **upload CSV files containing movie data**, store them in **MongoDB Atlas**, and retrieve them via a REST API with **pagination, filtering, and sorting**.

---
## 🚀 Features
- Upload CSV files and store movie data in **MongoDB Atlas**
- Retrieve movies with **pagination, sorting, and filtering by year & language**
- Well-structured **Flask backend**
- Uses **dotenv for environment variables**
- User-friendly **HTML templates for uploading and viewing data**

---
## 📂 Folder Structure
```
📦 Movie-Data-API
 ┣ 📂 templates        # HTML templates for UI
 ┣ 📂 uploads          # Folder to store uploaded CSV files
 ┣ 📜 app.py           # Main Flask application
 ┣ 📜 config.py        # Configuration settings
 ┣ 📜 .env             # Environment variables (MongoDB URI, etc.)
 ┣ 📜 requirements.txt # Dependencies
 ┣ 📜 README.md        # This documentation
```

---
## 🛠 Installation
Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/your-username/Movie-Data-API.git
$ cd Movie-Data-API
```

### 2️⃣ Set Up a Virtual Environment
```sh
$ python -m venv venv
$ source venv/bin/activate    # On MacOS/Linux
$ venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a **.env** file in the root directory and add the following:
```
MONGO_URI=mongodb+srv://your_username:your_password@cluster0.mongodb.net/movieDB?retryWrites=true&w=majority
FLASK_DEBUG=True
```
Replace **your_username**, **your_password**, and **movieDB** with your actual MongoDB Atlas credentials.

### 5️⃣ Run the Application
```sh
$ flask run
```
The app will be available at **http://127.0.0.1:5000/**

---
## 📝 API Endpoints

### 🔹 Upload CSV File
```
POST /upload
```
- **Description:** Uploads a CSV file and stores movie data in MongoDB.
- **Request:**
  - Form-data with `file` (CSV file)
- **Response:**
```json
{
    "message": "File uploaded successfully."
}
```

### 🔹 Get Movies
```
GET /movies?page=1&limit=10&year=2023&language=English&sort_by=release_date&order=asc
```
- **Description:** Retrieves movies with pagination, sorting, and filtering.
- **Query Params:**
  - `page` (default: 1)
  - `limit` (default: 10)
  - `year` (optional, filter by release year)
  - `language` (optional, filter by language)
  - `sort_by` (default: release_date)
  - `order` (asc/desc, default: asc)
- **Response:**
```json
[
    {
        "title": "Movie Title",
        "year": "2023",
        "languages": ["English", "French"],
        "release_date": "2023-05-20"
    }
]
```

---
## 📸 Screenshots

### 🔹 Upload Page
![Upload Page](screenshots/upload.png)

### 🔹 Movie List Page
![Movie List](screenshots/movies.png)

---
## 🤝 Contributing
1. **Fork** the repository
2. **Create a new branch** (`feature/your-feature`)
3. **Commit your changes** (`git commit -m 'Added new feature'`)
4. **Push to the branch** (`git push origin feature/your-feature`)
5. **Open a Pull Request**

---
## ⚖ License
This project is licensed under the **MIT License**.

---

### 🎯 Happy Coding! 🚀