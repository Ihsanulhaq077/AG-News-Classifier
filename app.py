import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Page setup
st.set_page_config(page_title="📰 AG News Classification Demo", page_icon="🗞️")

# Title and description
st.title("📰 AG News Classification Demo")
st.write("Enter a news headline or short description and see which category it belongs to.")

# Load trained model and vectorizer
model = joblib.load("svm_model.pkl")          # your best model (SVM)
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Input text box
text = st.text_area("Enter news text:")
# Step 1: Install pipreqs (only once)

  

# Predict button
if st.button("Predict"):
    if text.strip():
        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)[0]

        # category mapping
        category_map = {
            0: "World 🌍",
            1: "Sports 🏅",
            2: "Business 💼",
            3: "Sci/Tech 🔬"
        }
        category = category_map.get(prediction, "Unknown")

        st.success(f"**Prediction:** {category}")
    else:
        st.warning("Please enter some text first.")
 