import streamlit as st
import pickle
import string
import nltk
import sklearn
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer



nltk.download('stopwords')
ps = PorterStemmer()

# Stopwords list ko loop se bahar cache/store kar liya
stop_words = set(stopwords.words('english'))



def transform_text(text):
    text = str(text).lower()
    tokens = nltk.word_tokenize(text)
    
    y = []
    for i in tokens:
        if i.isalnum() and i not in stop_words and i not in string.punctuation:
            y.append(ps.stem(i))
            
    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter your message:")


if st.button('Predict'):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")