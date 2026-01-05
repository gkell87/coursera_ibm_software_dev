# Import Flask, render_template, request
from flask import Flask, request, render_template
"""Module for emotion detection script."""
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask('Emotion Detector')

# Assign route
@app.route('/emotionDetector')
def emo_analyzer():
    """Function to call emotion detector."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to function in EmotionDetection Module
    resp = emotion_detector(text_to_analyze)

    # Handle no response error
    if resp['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    # Return a formatted string with the Emotion, Score and Dominant Emotion
    return 'For the given statement, the system response is'.format(str(response)), 'The dominant emotion is'.format(response['dominant_emotion'])

# Assign route to render the index.html in the template folder
@app.route('/')
def render_index_page():
    """Function for rendering page"""
    return render_template('index.html')

# Assign host to run app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
