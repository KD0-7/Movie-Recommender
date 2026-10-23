# Cinematic Movie Recommender

A content-based movie recommendation system built with Python, Flask, and Tailwind CSS. The engine computes genre similarity using TF-IDF Vectorization and Cosine Similarity combined with weighted ratings to recommend the most relevant movies.

## 🚀 Features

- **Content-Based Filtering**: Uses TF-IDF vectorization on movie genres and cosine similarity.
- **Hybrid Scoring**: Combines similarity score (70%) with ratings (30%) for high-quality recommendations.
- **RESTful API**: Flask backend providing a `/api/recommend` endpoint.
- **Modern UI**: Clean, responsive frontend built with Tailwind CSS.

## 📁 Project Structure

```text
Movie-Recommender/
├── app.py                 # Flask server & API endpoints
├── recommender.py         # Recommendation model & TF-IDF logic
├── movie_recommender.html # Web interface
├── requirements.txt       # Project dependencies
├── data/
│   └── movies.csv         # Movie dataset
└── .gitignore             # Git ignore configuration
```

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KD0-7/Movie-Recommender.git
   cd Movie-Recommender
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```
   The server will start at `http://127.0.0.1:5000`.

5. **Open the frontend**:
   Open `movie_recommender.html` in your web browser, enter a movie title, and view recommendations.

## 📄 License

This project is licensed under the MIT License.
