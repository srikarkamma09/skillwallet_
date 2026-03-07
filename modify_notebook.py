import json

with open('Hypertension_Prediction_System.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Cell 22: Feature Engineering & Selection
feature_engineering_text = """---
## 4. Feature Engineering & Selection

**Label Encoding Applied:**
* Gender: Male=0, Female=1
* Binary features: No=0, Yes=1
* Age groups: 18-34=1, 35-50=2, 51-64=3, 65+=4
* Severity: Mild=0, Moderate=1, Severe=2
* Blood pressure ranges: Encoded as ordinal values
* Target stages: Normal=0, Stage-1=1, Stage-2=2, Crisis=3

**Feature Scaling:** Applied MinMaxScaler to ordinal features for optimal model performance."""

# Find Cell 22
markdown_idx = 0
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        if "## 4. Feature Engineering" in ''.join(cell['source']):
            nb['cells'][i]['source'] = [line + '\n' for line in feature_engineering_text.split('\n')]
            break

# 2. Update Cell 12: Visual Analysis
visual_analysis_text = """### 3.2 Visual Analysis

**1. Gender Distribution**
A count plot and pie chart were used to visualize the distribution of genders in the dataset.
The count plot (Figure 1) revealed that the dataset contains an almost equal representation of male and female patients, ensuring balanced demographic coverage for analysis.
The pie chart (Figure 2) further confirmed this observation, showing near 50–50 distribution between genders. This balance minimizes gender bias during model training and interpretation.

**2. Hypertension Stages Distribution**
A bar chart was used to display the count of patients across different hypertension stages.
The plot showed that Stage-1 hypertension is the most prevalent category, representing the majority of patients in the dataset. Stages 2 and 3 were less frequent, indicating fewer cases of severe hypertension. This insight suggests that most patients in the dataset are in the early phase of the condition, making early intervention analysis feasible.

**3. Correlation between Systolic and Diastolic Pressure**
A heatmap (Figure 4) was plotted to examine the relationship between the numeric representations of systolic and diastolic blood pressure (converted from categorical ranges to midpoints).
The heatmap displayed a strong positive correlation between systolic and diastolic values, as expected in physiological data — indicating that as systolic pressure increases, diastolic pressure also tends to rise proportionally. This validates the integrity of the recorded measurements.

**4. TakeMedication vs. Severity**
A count plot (Figure 5) was created to explore the relationship between medication status and hypertension severity.
The visualization showed that patients taking medication were predominantly in higher severity categories, whereas those not on medication were more frequent in lower stages or normal conditions. This trend implies a logical connection between treatment status and disease intensity.

**5. Age Group vs. Hypertension Stages**
Another count plot (Figure 6) was used to examine how age groups are distributed across different hypertension stages.
The analysis revealed that middle-aged and elderly individuals had a higher prevalence of Stage-1 and Stage-2 hypertension compared to younger patients. This pattern aligns with medical expectations that hypertension risk increases with age, highlighting the importance of preventive screening for older populations.

**6. Pairplot: Systolic vs. Diastolic across Stages**
A pairplot (Figure 7) was generated to study the multivariate relationship between systolic and diastolic blood pressure across different hypertension stages.
Distinct clusters were visible, indicating that patients with higher systolic and diastolic values tend to belong to higher hypertension stages. The distribution patterns across the diagonal density plots also confirmed increasing spread with disease severity, suggesting progressive blood pressure elevation as hypertension advances."""

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        if "### 3.2 Visual Analysis" in ''.join(cell['source']):
            nb['cells'][i]['source'] = [line + '\n' for line in visual_analysis_text.split('\n')]
            break


# 3. Update Cell 30 or similar: Model Testing
model_testing_text = """---
## 7. Performance Testing & Model Selection
### Description: Comprehensive Model Testing
We implemented and evaluated seven different machine learning algorithms to identify the most suitable approach for hypertension prediction:

**1. Logistic Regression**
* Results: Accuracy: 95.2%
* Precision: High for all classes
* Recall: Excellent performance across stages

**2. Decision Tree Classifier**
* Results: Accuracy: 100%
* Performance: Perfect classification on test set
* Concern: Potential overfitting indicated

**3. Random Forest Classifier**
* Results: Accuracy: 100%
* Performance: Perfect classification
* Concern: Signs of overfitting

**4. Support Vector Machine (SVM)**
* Results: Accuracy: 100%
* Performance: Perfect classification
* Concern: Potential overfitting

**5. K-Nearest Neighbors (KNN)**
* Results: Accuracy: 98.1%
* Performance: Strong but not perfect
* Assessment: Good generalization

**6. Ridge Classifier**
* Results: Accuracy: 90.0%
* Performance: Solid baseline performance
* Assessment: Good generalization capability

**7. Gaussian Naive Bayes (Selected Model)**"""

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        if "## 7. Performance Testing & Model Selection" in ''.join(cell['source']):
            # let's just append or replace. The original has:
            # ---
            # ## 7. Performance Testing & Model Selection
            # ### 7.1 Evaluation Metrics Comparison
            # I will just replace it entirely with the model_testing_text, plus the subtitle
            full_text = model_testing_text + "\n\n### 7.1 Evaluation Metrics Comparison"
            nb['cells'][i]['source'] = [line + '\n' for line in full_text.split('\n')]
            break

with open('Hypertension_Prediction_System.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook modified successfully.")
