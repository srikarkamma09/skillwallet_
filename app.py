from flask import Flask, render_template, request, jsonify
import joblib, pandas as pd, json

app = Flask(__name__)
model = joblib.load('database/best_hypertension_model.pkl')
label_encoder = joblib.load('database/label_encoder.pkl')
with open('config/model_metadata.json') as f:
    metadata = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', metadata=metadata)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)
    stage = label_encoder.inverse_transform(prediction)[0]
    probs = model.predict_proba(input_df)[0]
    prob_dict = {label_encoder.inverse_transform([i])[0]: round(float(p),4) for i,p in enumerate(probs)}
    risk = round(float(max(probs)*100), 1)
    sl = str(stage).lower()
    if 'normal' in sl or 'pre' in sl:
        urgency, recs = 'LOW', ['Maintain balanced diet','Exercise 150 min/week','Monitor BP weekly']
    elif 'stage-1' in sl or 'stage 1' in sl or sl=='1':
        urgency, recs = 'MODERATE', ['Begin lifestyle modifications','Follow DASH diet','Reduce sodium','Monitor BP daily']
    elif 'stage-2' in sl or 'stage 2' in sl or sl=='2':
        urgency, recs = 'HIGH', ['Consult physician immediately','Medication likely required','Daily BP monitoring']
    else:
        urgency, recs = 'CRITICAL', ['Seek immediate medical attention','Follow prescribed medications','Continuous monitoring']
    return jsonify({'predicted_stage':stage,'risk_score':risk,'probabilities':prob_dict,'urgency':urgency,'recommendations':recs})

if __name__ == '__main__':
    app.run(debug=True, port=5000)