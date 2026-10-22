# 📧 Email Spam Classifier

A machine-learning web application that classifies email or SMS text as **Spam** or **Not Spam**. The project uses natural language processing (NLP), a trained text-vectorization pipeline, and a Streamlit interface for real-time predictions.

## 🚀 Features

- Classifies messages as **Spam** or **Not Spam**
- Interactive web interface built with **Streamlit**
- Pre-trained machine-learning model (`model.pkl`)
- Text feature extraction using `vectorizer.pkl`
- Data exploration, preprocessing, and model training in a Jupyter Notebook
- Uses the SMS Spam Collection dataset (`spam.csv`)

## 🧠 How It Works

1. The user enters an email/SMS message in the Streamlit app.
2. The text is cleaned and tokenized using NLTK.
3. The saved vectorizer converts the text into numerical features.
4. The trained classifier predicts whether the message is spam.
5. The result is displayed instantly in the browser.

## 📁 Project Structure

```text
Email-spam-classifier/
│
├── app.py                      # Streamlit web application
├── model.pkl                   # Trained machine-learning model
├── vectorizer.pkl              # Saved text vectorizer
├── requirements.txt            # Python dependencies
├── sms-spam-detection.ipynb    # Data analysis and model training notebook
├── spam.csv                    # SMS spam dataset
└── README.md                   # Project documentation
```

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — Web application
- **scikit-learn** — Machine learning and vectorization
- **NLTK** — Text preprocessing and tokenization
- **Pandas / NumPy** — Data handling
- **Jupyter Notebook** — Model development and experimentation

## ⚙️ Installation

1. Clone the repository:

```bash
git clone [https://github.com/prashantrao44/Email-spam-classifier.git](https://github.com/prashantrao44/Email-spam-classifier.git)
cd Email-spam-classifier
