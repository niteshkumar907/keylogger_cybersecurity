# Install required libraries: pip install textblob matplotlib

from textblob import TextBlob
import matplotlib.pyplot as plt

# Function to analyze sentiment
def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Input method: Getting multiple user inputs
print("Enter text to analyze sentiment (type 'exit' to stop):")
texts = []
while True:
    user_input = input("Enter text: ")
    if user_input.lower() == 'exit':
        break
    texts.append(user_input)

# Analyze sentiment for each text and store polarity values
polarities = [analyze_sentiment(text) for text in texts]

# Print sentiment analysis results
for text, polarity in zip(texts, polarities):
    print(f"Text: {text}\nPolarity: {polarity}\n")

# Plotting polarity of each text
plt.bar(range(len(texts)), polarities, color='blue')
plt.xticks(range(len(texts)), texts, rotation=45, ha="right")
plt.ylabel("Polarity")
plt.title("Sentiment Analysis")
plt.show()
