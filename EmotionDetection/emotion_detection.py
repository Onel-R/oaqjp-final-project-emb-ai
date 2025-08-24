import requests, json, pprint

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    formatted = json.loads(response.text)
    #print(response.status_code)
    #pprint.pprint(formatted)

    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None}

    anger_score = formatted['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted['emotionPredictions'][0]['emotion']['sadness']
    scores = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 
            'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': max(scores, key=scores.get)}
