# 🎓 Course Recommendation System

A simple and interactive **Content-Based Recommendation System** that suggests similar Udemy courses based on their title, subject, and difficulty level.

Built using **Streamlit**, **TF-IDF Vectorization**, and **Cosine Similarity**, this project demonstrates the working of a modern recommender system in an intuitive dashboard format.

---

## 🧩 Project Overview

The goal of this project is to help learners find similar online courses based on their interests.  
It uses **Natural Language Processing (NLP)** techniques to measure similarity between course descriptions and subjects.

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit** (for UI dashboard)
- **Pandas**
- **Scikit-learn** (TF-IDF & cosine similarity)
- **Matplotlib** (for visualization)

---

## 📂 Project Structure

course-recommender/
│
├── app.py # Streamlit dashboard
├── udemy_course_data.csv # Udemy dataset used for recommendations
├── Course_Recommender_Colab.ipynb # Colab notebook (model building & analysis)
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

---

## 📊 Dataset

The dataset is sourced from [Kaggle – Course Recommendation System Dataset](https://www.kaggle.com/datasets/shailx/course-recommendation-system-dataset).  
It contains Udemy course data with fields like:
- `course_id`
- `course_title`
- `subject`
- `price`
- `num_subscribers`
- `num_reviews`
- `level`
- `content_duration`
- `published_timestamp`

---

## ⚙️ How It Works

1. Loads and cleans course data.  
2. Combines relevant columns like title, subject, and level into one feature.  
3. Uses **TF-IDF Vectorization** to convert text into vectors.  
4. Calculates **Cosine Similarity** to find related courses.  
5. Displays the top 5 similar courses on a Streamlit interface.

---

## 🚀 Getting Started

### 🔧 Prerequisites
Ensure Python 3.10+ is installed on your system.

### 🪜 Installation
Clone the repository:
```bash
git clone https://github.com/ishan29jain/course-recommender-system.git
cd course-recommender-system
