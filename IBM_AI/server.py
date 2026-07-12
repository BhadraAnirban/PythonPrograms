
"""
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the flask app
app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Receives text from the HTML interface and runs sentiment analysis.
    Returns the label and confidence score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    analyzer_response = sentiment_analyzer(text_to_analyze)

    print(analyzer_response)

    label = analyzer_response['label']
    score = analyzer_response['score']

    if label is None:
        return "Invalid input! Try again."

    sentiment = label.split('_')[1]
    return (
        f"The given text has been identified as {sentiment} "
        f"with a score of {score}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    # Execute the flask app on localhost:5001
    app.run(host="0.0.0.0", port=5001)
