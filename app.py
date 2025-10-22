import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Page setup
st.set_page_config(page_title="📰 AG News Classification Demo", page_icon="🗞️")

# Title and description
st.title("📰 AG News Classification Demo")
st.write("Enter a news headline or short description and see which category it belongs to.")

# Load trained model and vectorizer
model = joblib.load("svm_model.pkl")          # your best model (SVM)
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Preprocessing function to match notebook
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove punctuation
    stop_words = set(stopwords.words('english'))  # Load stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

# Input text box
text = st.text_area("Enter news text:")

# Predict button
if st.button("Predict"):
    if text.strip():
        # Preprocess the input text
        processed_text = preprocess_text(text)
        # Vectorize the preprocessed text
        text_vec = vectorizer.transform([processed_text])
        # Make prediction
        prediction = model.predict(text_vec)[0]

        # Category mapping
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