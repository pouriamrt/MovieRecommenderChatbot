# 🎬 Movie Recommender Chatbot

An intelligent movie chatbot assistant that recommends movies using conversational input via Dialogflow, Flask as the backend, and several content-based filtering techniques using TF-IDF and similarity metrics.

---

## 🤖 Features

- Conversational interface powered by Dialogflow (Google NLP)
- Flask backend to handle webhook and response logic
- Multiple recommender modules (`recommender1.py` to `recommender5.py`)
- Uses TF-IDF, cosine similarity, and metadata for smart suggestions
- Reads movie datasets using `pandas`
- Easy integration with Dialogflow fulfillment

---

## 🧠 Technologies Used

| Component     | Stack/Library                 |
|---------------|-------------------------------|
| Chatbot       | Dialogflow                    |
| Backend       | Flask                         |
| NLP/ML        | TF-IDF, cosine similarity, scikit-learn |
| Data Handling | pandas                        |
| Hosting       | Local or Cloud via Flask      |

---

## 📁 Project Structure

```bash
MovieRecommenderChatbot/
├── app.py               # Flask app handling webhook routes
├── recommender1.py      # Recommender using TF-IDF + cosine similarity
├── recommender2.py      # Alternative recommender logic
├── recommender3.py      # [Optional/Unused]
├── recommender4.py      # Based on different feature extraction
├── recommender5.py      # Experimental recommender
├── requirements.txt     # Dependencies
├── LICENSE
└── README.md
```

---

## ⚙️ Setup & Run

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Run the Flask backend**
```bash
python app.py
```

3. **Connect to Dialogflow**
- Go to Dialogflow > Fulfillment
- Enable webhook and set the URL to your Flask server (e.g., `https://yourserver.com/webhook`)
- Create intents and configure them to trigger the Flask webhook

---

## 🧪 Example Usage

**User**: *Can you suggest a sci-fi movie like Interstellar?*  
**Bot**: *You might enjoy "The Martian" or "Gravity". Want more like that?*

---

## 📌 Notes

- Each recommender file implements a different recommendation strategy
- Ideal for experimenting with different movie recommendation models
- Data should be loaded inside the recommender scripts (`pandas.read_csv`)
- Currently configured for English-language movie metadata

---

## 📄 License

MIT License © 2025 Pouria Mortezaagha
