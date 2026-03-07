# 🩺 Hypertension Prediction & Clinical Assessment System

A professional, end-to-end medical decision-support system designed to predict and classify stages of hypertension using clinical parameters and lifestyle data.

## 🚀 Overview
This project combines a robust machine learning pipeline with a premium web-based assessment tool. It allows healthcare providers or at-risk individuals to quickly evaluate hypertension risk levels and receive personalized clinical recommendations.

### Key Components
1. **Clinical Assessment Tool**: A Flask-based web application featuring a modern, hospital-grade UI with glassmorphism and intuitive clinical dropdowns.
2. **Machine Learning Pipeline**: A scikit-learn based research path that evaluates multiple classifiers (Logistic Regression, Random Forest, SVM, etc.) and exports the best-performing model.
3. **Research Analysis**: A streamlined Jupyter Notebook containing exactly the 6 high-impact clinical visualizations required for deployment reporting.

## 📊 Research Data & Insights
The research notebook (`Hypertension_Prediction_System.ipynb`) provides data-driven evidence for the classification logic, focusing on:
- **Gender Distribution**: Demographic breakdown of the patient population.
- **Hypertension Stages**: Distribution of condition severity (Normal to Stage-2).
- **Pressure Correlations**: Statistical relationship between Systolic and Diastolic readings.
- **Medication Impact**: Analysis of medication status vs. condition severity.
- **Age-Based Risk**: Identifying high-risk age groups across various stages.
- **Bi-variate Pairplots**: Deep dives into the feature relationships segmented by clinical stage.

## 🛠️ Technology Stack
- **Frontend**: HTML5, Vanilla CSS (Premium Responsive Design), FontAwesome.
- **Backend**: Python, Flask.
- **AI/ML**: Scikit-Learn, Pandas, NumPy, Joblib.
- **Visualization**: Seaborn, Matplotlib.

## ⚙️ Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/hypertension-prediction.git
   cd hypertension-prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```
   Access the system at `http://localhost:5000`

## ⚖️ Disclaimer
This system is intended for **decision-support and educational purposes only**. It does NOT provide medical diagnosis. Always consult with a qualified healthcare professional for medical advice, diagnosis, or treatment.
