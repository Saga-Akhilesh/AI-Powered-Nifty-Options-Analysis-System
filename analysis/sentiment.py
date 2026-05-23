from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

def get_sentiment(text):

    result = sentiment_model(text[:512])

    label = result[0]["label"]

    if label == "positive":
        return 1

    if label == "negative":
        return -1

    return 0