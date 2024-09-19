from flask import Flask, request, jsonify
from textblob import TextBlob
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    text = data.get('text')
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    out = "Positive" if polarity > 0 else "Negative"
    return jsonify({"feedback": out})


if __name__ == '__main__':
    app.run(debug=True)
