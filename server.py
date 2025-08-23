from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emo_detector():
    text_To_Analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_To_Analyze)