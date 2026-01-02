# Import Flask, render_template, request
from flask import Flask, request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer """analzes sentiment"""

# Initiate the flask app
app = Flask('Sentiment Analyzer')

# Assign route
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to function in SentimentAnalysis Module
    response = sentiment_analyzer(text_to_analyze)

    # Extract the lable nad score repsonse
    label = response['label']
    score = response['score']

     # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."

    # Return a formatted string with the sentiment label and score
    return "The given text is {} with a score of {}.".format(label.split('_')[1], score)

# Assign route to render the index.html in the template folder
@app.route("/")
def render_index_page():
    return render_template('index.html')

# Assign host to run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
