import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')  # Only needed once

# Load the vectorizer and model
vector_form = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

port_stem = PorterStemmer()

def stemming(content):
    con = re.sub('[^a-zA-Z]', ' ', content)
    con = con.lower()
    con = con.split()
    con = [port_stem.stem(word) for word in con if word not in stopwords.words('english')]
    return ' '.join(con)

def fake_news(news):
    news = stemming(news)
    input_data = [news]
    vector_form1 = vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction

# Streamlit UI
st.title('📰 Fake News Classification App')
st.subheader("Input the News Content Below")
sentence = st.text_area("Enter your news content here", "", height=200)
predict_btt = st.button("Predict")

if predict_btt:
    if sentence.strip() == "":
        st.warning("Please enter some text before prediction.")
    else:
        prediction_class = fake_news(sentence)
        st.text("Processing...")
        st.text("Done!")
        st.text("Prediction:")
        
        if prediction_class == [0]:
            st.success('✅ Reliable News')
        elif prediction_class == [1]:
            st.error('❌ Unreliable / Fake News')
