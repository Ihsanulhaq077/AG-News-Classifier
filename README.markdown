# AG News Classifier: Streamlit-Powered Text Classification

## Overview
This project is a web-based application that classifies news headlines or short descriptions into one of four categories: **World**, **Sports**, **Business**, or **Sci/Tech**. Built with **Streamlit**, it uses a pre-trained **Support Vector Machine (SVM)** model and **TF-IDF vectorization** to deliver accurate predictions. The app provides an intuitive interface for users to input text and instantly see the predicted category, making it a great tool for exploring text classification and NLP.

## Features
- **User-Friendly Interface**: Input news text via a Streamlit text area and get instant predictions.
- **Pre-Trained Model**: Utilizes a high-performing SVM model trained on the AG News dataset.
- **TF-IDF Vectorization**: Converts text into numerical features for robust classification.
- **Category Mapping**: Outputs predictions as human-readable categories (World 🌍, Sports 🏅, Business 💼, Sci/Tech 🔬).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ag-news-classifier.git
   cd ag-news-classifier
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the pre-trained model (`svm_model.pkl`) and vectorizer (`tfidf_vectorizer.pkl`) are in the project directory.
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Dependencies
- Python 3.8+
- Streamlit
- scikit-learn
- joblib

## Usage
1. Launch the app using `streamlit run app.py`.
2. Enter a news headline or short description in the text area.
3. Click the **Predict** button to see the predicted category.
4. If no text is entered, a warning will prompt for input.

## Example
**Input**: "New AI breakthrough in quantum computing announced at tech conference"
**Output**: Sci/Tech 🔬

## Project Structure
- `app.py`: Main Streamlit application script.
- `svm_model.pkl`: Pre-trained SVM model.
- `tfidf_vectorizer.pkl`: Pre-trained TF-IDF vectorizer.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Future Improvements
- Add support for batch predictions.
- Include model performance metrics (e.g., accuracy, F1 score) in the app.
- Deploy the app to a cloud platform for public access.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for bug fixes, feature additions, or improvements.

## License
This project is licensed under the MIT License.

## Contact
Connect with me on [LinkedIn](https://www.linkedin.com/in/your-profile) or open an issue for questions or feedback!