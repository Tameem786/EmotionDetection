import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Define the text to be analyzed
text = "I am feeling very happy today!"

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Get the sentiment scores
scores = sia.polarity_scores(text)

# Extract the compound score
compound_score = scores["compound"]

# Determine the emotion based on the compound score
if compound_score >= 0.5:
    emotion = "positive"
elif compound_score > -0.5 and compound_score < 0.5:
    emotion = "neutral"
else:
    emotion = "negative"

print("The emotion in the text is:", emotion)
