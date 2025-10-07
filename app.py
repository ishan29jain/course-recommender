import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import matplotlib.pyplot as plt

# ----------------------------
# Load Dataset
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("/Users/ishanjain/Downloads/course-recommender/udemy_course_data.csv")
    df = df.fillna('')
    df['combined'] = df['course_title'] + ' ' + df['subject'] + ' ' + df['level']
    return df

df = load_data()

# ----------------------------
# Build TF-IDF Matrix
# ----------------------------
vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(df['combined'])
similarity = cosine_similarity(vectors)

# ----------------------------
# Recommendation Function
# ----------------------------
def recommend(course_title):
    course_list = df['course_title'].tolist()
    closest_match = difflib.get_close_matches(course_title, course_list, n=1)
    
    if not closest_match:
        return None, []
    
    title = closest_match[0]
    idx = df[df['course_title'] == title].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended = [df.iloc[i[0]]['course_title'] for i in sorted_scores]
    return title, recommended

# ----------------------------
# Streamlit App Layout
# ----------------------------
st.set_page_config(page_title="🎓 Course Recommendation System", layout="centered")
st.title("🎓 Course Recommendation System")
st.markdown("Discover similar Udemy courses based on content similarity using **TF-IDF** and **Cosine Similarity**.")

course_titles = df['course_title'].tolist()
selected_course = st.selectbox("Select or search a course:", course_titles)

if st.button("Recommend"):
    title, recs = recommend(selected_course)
    
    if recs:
        st.subheader(f"Courses similar to: **{title}**")
        for r in recs:
            st.write(f"- {r}")
    else:
        st.warning("No similar courses found. Try another title.")

# ----------------------------
# Visualization (Optional)
# ----------------------------
if st.button("Visualize Similarity"):
    title, recs = recommend(selected_course)
    if recs:
        idx = df[df['course_title'] == title].index[0]
        scores = list(enumerate(similarity[idx]))
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
        names = [df.iloc[i[0]]['course_title'] for i in sorted_scores]
        values = [i[1] for i in sorted_scores]

        fig, ax = plt.subplots()
        ax.barh(names, values)
        ax.set_xlabel("Similarity Score")
        ax.set_title(f"Top 5 Similar Courses to '{title}'")
        ax.invert_yaxis()
        st.pyplot(fig)

st.markdown("---")
st.caption("Developed by Ishan Jain | Content-based Recommender System")