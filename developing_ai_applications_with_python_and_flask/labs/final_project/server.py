# Import Flask, render_template, request
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask('Emotion Detector')

# Assign route
@app.route('/emotionDetector')
def emo_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to function in EmotionDetection Module
    response = emotion_detector(text_to_analyze)

    # Return a formatted string with the Emotion, Score and Dominant Emotion
    return 'For the given statement, the system response is'.format(str(response)), 'The dominant emotion is'.format(response['dominant_emotion'])

# Assign route to render the index.html in the template folder
@app.route('/')
def render_index_page():
    return render_template('index.html')

# Assign host to run app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)