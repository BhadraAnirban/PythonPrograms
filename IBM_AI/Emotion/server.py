
"""
Flask application for detecting emotions in user-provided text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the provided text and return the detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    detector_response = emotion_detector(text_to_analyze)

    if detector_response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    return (
        f"For the given statement, the system response is "
        f"'anger': {detector_response['anger']}, "
        f"'disgust': {detector_response['disgust']}, "
        f"'fear': {detector_response['fear']}, "
        f"'joy': {detector_response['joy']} and "
        f"'sadness': {detector_response['sadness']}. "
        f"The dominant emotion is "
        f"<b>{detector_response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
