# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on your selection.

## 🚀 Live Demo
👉 [Click here to try the app](https://movie-recommender-system-e2cvztpnlw5l9uzo6askgv.streamlit.app/)

## 📌 Features
- Select any movie from 5000+ movies
- Get Top 5 similar movie recommendations instantly

## 🛠️ Tech Stack
- Python, Pandas, Scikit-learn, NLTK, Streamlit

## ⚙️ How it Works
1. Movie metadata combined into tags
2. Tags preprocessed using stemming
3. TF-IDF Vectorization applied
4. Cosine Similarity used to find similar movies
5. Top 5 recommendations returned

## 🧠 Algorithm
```
Raw Movie Data
      ↓
Data Preprocessing (stemming, stop words removal)
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity Matrix
      ↓
Top 5 Recommendations
```
