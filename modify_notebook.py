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
            start_idx = i
            break

# remove cells between visual analysis and feature engineering headings
end_idx = None
for j, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and "## 4. Feature Engineering" in ''.join(cell['source']):
        end_idx = j
        break
if end_idx is not None and start_idx is not None:
    # delete cells in range (start_idx+1, end_idx)
    for k in range(end_idx-1, start_idx, -1):
        nb['cells'].pop(k)

# insert new code cell with required plots after visual analysis cell
plot_code = '''# Viz: only the requested plots

# mapping tables for conversions
age_map = {'18-34': 26, '35-50': 42.5, '51-64': 57.5, '65+': 70}
systolic_map = {'90 - 100': 95, '101 - 110': 105, '111 - 120': 115, '121 - 130': 125, '131 - 140': 135, '141 - 150': 145, '151 - 160': 155, '161 - 170': 165, '171 - 180': 175, '181 - 190': 185, '191 - 200': 195}
diastolic_map = {'51 - 60': 55.5, '61 - 70': 65.5, '70 - 80': 75, '81 - 90': 85, '91 - 100': 95, '101 - 110': 105, '111 - 120': 115, '121 - 130': 125, '131 - 140': 135, '141 - 150': 145}

df_plot = df.copy()
df_plot['Age_num'] = df_plot['Age'].map(age_map)
df_plot['Systolic_num'] = df_plot['Systolic'].map(systolic_map)
df_plot['Diastolic_num'] = df_plot['Diastolic'].map(diastolic_map)

# 1. Gender Distribution
fig, axs = plt.subplots(1, 2, figsize=(12,5))
sns.countplot(data=df, x='Gender', ax=axs[0], palette='pastel')
axs[0].set_title('Gender Count')
df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', ax=axs[1],
                                      colors=sns.color_palette('pastel'),
                                      startangle=90, label='')
axs[1].set_title('Gender Proportion')
axs[1].set_ylabel('')
plt.tight_layout()
plt.savefig('gender_distribution.png', dpi=150, bbox_inches='tight')
plt.show()

# 2. Hypertension Stages Distribution
fig, ax = plt.subplots(figsize=(8,5))
sns.countplot(data=df, x='Stages', ax=ax, palette='viridis', edgecolor='black')
ax.set_title('Distribution of Hypertension Stages', fontsize=14, fontweight='bold')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontweight='bold', xytext=(0, 5),
                textcoords='offset points')
plt.tight_layout()
plt.savefig('stage_distribution.png', dpi=150, bbox_inches='tight')
plt.show()

# 3. Correlation between Systolic and Diastolic
corr = df_plot[['Systolic_num','Diastolic_num']].corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0)
plt.title('Systolic vs Diastolic Correlation')
plt.tight_layout()
plt.savefig('systolic_diastolic_corr.png', dpi=150, bbox_inches='tight')
plt.show()

# 4. TakeMedication vs. Severity
fig, ax = plt.subplots(figsize=(8,5))
sns.countplot(data=df, x='TakeMedication', hue='Stages', ax=ax, palette='viridis')
ax.set_title('Medication Status vs Hypertension Stages')
plt.tight_layout()
plt.savefig('medication_severity.png', dpi=150, bbox_inches='tight')
plt.show()

# 5. Age Group vs Hypertension Stages
fig, ax = plt.subplots(figsize=(10,5))
sns.countplot(data=df, x='Age', hue='Stages', ax=ax, palette='Set2')
ax.set_title('Age Group vs Hypertension Stages')
plt.tight_layout()
plt.savefig('age_stage_count.png', dpi=150, bbox_inches='tight')
plt.show()

# 6. Pairplot: Systolic vs Diastolic across stages
sns.pairplot(df_plot[['Systolic_num','Diastolic_num','Stages']], hue='Stages',
             palette='viridis', diag_kind='kde',
             plot_kws={'alpha':0.6, 'edgecolor':'black', 'linewidth':0.3})
plt.suptitle('Pairplot of Systolic and Diastolic by Stage', fontsize=16, fontweight='bold', y=1.02)
plt.savefig('pairplot.png', dpi=150, bbox_inches='tight')
plt.show()
'''

new_cell = {
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': [line + '\n' for line in plot_code.split('\n')]
}
nb['cells'].insert(start_idx + 1, new_cell)


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
