import pandas as pd
import string
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Text preprocessing
def clean_text(text):
    text = text.lower()
    text = ''.join(c for c in text if c not in string.punctuation)
    return text

class SpamClassifier:
    def __init__(self, model_file='spam_model.pkl', vectorizer_file='vectorizer.pkl'):
        self.model_file = model_file
        self.vectorizer_file = vectorizer_file
        self.model = None
        self.vectorizer = None

    def train(self, csv_path):
        try:
            df = pd.read_csv(csv_path)
            df['cleaned'] = df['message'].apply(clean_text)

            self.vectorizer = CountVectorizer()
            X = self.vectorizer.fit_transform(df['cleaned'])
            y = df['label']

            self.model = MultinomialNB()
            self.model.fit(X, y)

            with open(self.model_file, 'wb') as f:
                pickle.dump(self.model, f)
            with open(self.vectorizer_file, 'wb') as f:
                pickle.dump(self.vectorizer, f)

            print("Model trained and saved successfully.")
        except Exception as e:
            print(f"Error during training: {e}")

    def load_model(self):
        try:
            with open(self.model_file, 'rb') as f:
                self.model = pickle.load(f)
            with open(self.vectorizer_file, 'rb') as f:
                self.vectorizer = pickle.load(f)
            print("Model loaded successfully.")
        except FileNotFoundError:
            print("Trained model not found. Please train it first.")
        except Exception as e:
            print(f"Error loading model: {e}")

    def predict_generator(self, messages):
        if not self.model or not self.vectorizer:
            raise Exception("Model not loaded.")
        for msg in messages:
            cleaned = clean_text(msg)
            vect = self.vectorizer.transform([cleaned])
            prediction = self.model.predict(vect)[0]
            yield msg, prediction

if __name__ == "__main__":
    clf = SpamClassifier()

    if not os.path.exists("spam_model.pkl"):
        csv_file = input("Enter path to training CSV file (e.g. spam.csv): ")
        clf.train(csv_file)
    else:
        clf.load_model()

    print("\nEnter messages to test (type 'exit' to stop):")
    test_messages = []
    while True:
        msg = input("Message: ")
        if msg.lower() == "exit":
            break
        test_messages.append(msg)

    print("\n--- Predictions ---")
    try:
        for msg, pred in clf.predict_generator(test_messages):
            print(f"[{pred.upper()}] {msg}")
    except Exception as e:
        print(f"Prediction error: {e}")
