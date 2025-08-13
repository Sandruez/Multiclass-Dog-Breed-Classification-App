# 🐟 Multiclass Fish Image Classification

## 📌 Project Overview
This project focuses on **multiclass fish species classification** using **deep learning** and **transfer learning** techniques.  
We trained and evaluated multiple models — both from scratch and using **pretrained architectures** such as **VGG16, ResNet50, MobileNetV2, InceptionV3, and EfficientNetB0** — to identify the best-performing model for this task.

---

## 📂 Dataset
- **Total Classes:** Multiple fish species (multiclass classification)
- **Train Data:** ~7,000 images
- **Validation Data:** ~1,000 images
- **Image Size:** 224×224 (resized for model input)
- **Batch Size:** 32

---

## 🛠️ Models Trained
We trained two categories of models:
1. **From Scratch:** Custom CNN architecture.
2. **Transfer Learning:** Pretrained models fine-tuned on our dataset.
3.    Training Strategy:
          Phase 1: Freeze base model, train only top layers
          Phase 2: Unfreeze and fine-tune all layers
---

## 📊 Model Results

### 1️⃣ Scratch Model Performance
| Metric        | Value   |
|---------------|---------|
| Accuracy      | 0.9730  |
| Precision     | 0.9691  |
| Recall        | 0.9730  |
| F1-Score      | 0.9709  |
| Validation Accuracy | 97.62% |
| Validation Loss     | 0.1078 |

---

### 2️⃣ Transfer Learning Models Performance

| Model            | Accuracy     | Precision    | Recall       | F1-score     |
|------------------|-------------|-------------|-------------|-------------|
| **VGG16**        | 0.9962      | 0.9961      | 0.9962      | 0.9961      |
| **ResNet50**     | 0.9984      | 0.9984      | 0.9984      | 0.9984      |
| **MobileNetV2**  | 0.9962      | 0.9963      | 0.9962      | 0.9960      |
| **InceptionV3**  | 0.9965      | 0.9966      | 0.9965      | 0.9963      |
| **EfficientNetB0**| 0.9947      | 0.9943      | 0.9947      | 0.9944      |

---

### 3️⃣ Best and Final Model Results (On Test Dataset)

#### **VGG16**
- **Best Model:** Accuracy: 0.9962 | Loss: 0.0142  
- **Final Model:** Accuracy: 0.9962 | Loss: 0.0142  

#### **ResNet50**
- **Best Model:** Accuracy: 0.9962 | Loss: 0.0118  
- **Final Model:** Accuracy: 0.9962 | Loss: 0.0118  

#### **InceptionV3**
- **Best Model:** Accuracy: 0.9965 | Loss: 0.0292  
- **Final Model:** Accuracy: 0.9965 | Loss: 0.0292  

#### **EfficientNetB0**
- **Best Model:** Accuracy: 0.9724 | Loss: 0.1177  
- **Final Model:** Accuracy: 0.9724 | Loss: 0.1177  

---

## 📈 Insights

- **ResNet50** delivered the **highest accuracy (99.84%)** and minimal loss, making it the **best performing model** overall.
- **VGG16** and **InceptionV3** also achieved near-perfect results, with very small differences in performance.
- **MobileNetV2** proved to be highly efficient with competitive accuracy while being lighter and faster to train.
- **EfficientNetB0**, though slightly behind in accuracy, offered a good trade-off between model size and performance.
- The **scratch CNN model** performed well (97.30% accuracy), but transfer learning models significantly outperformed it, showing the advantage of leveraging pretrained architectures.

---

## Model Performance Summary(On Train and Validation Dataset)

The table below compares training accuracy and validation accuracy for each model.  
A small gap between the two indicates **good generalization** (balanced fit), while a large positive gap (train much higher than val) would indicate **overfitting**.

| Model            | Train Acc | Val Acc | Gap     | Status                     |
|------------------|-----------|---------|---------|----------------------------|
| **Scratch**      | 93.77%    | 97.62%  | +3.85%  | Balanced / slight underfit |
| **VGG16**        | 99.68%    | 99.63%  | -0.05%  | Balanced                   |
| **ResNet50**     | 99.76%    | 99.82%  | -0.06%  | Balanced                   |
| **MobileNetV2**  | 99.20%    | 99.45%  | -0.25%  | Balanced                   |
| **InceptionV3**  | 98.12%    | 98.71%  | -0.59%  | Balanced                   |
|**EfficientNetB0**| 98.94%    | 98.99%  | -0.05%  | Balanced                   |

### Insights
- All models show **balanced performance** — validation accuracy is very close to training accuracy.  
- The **scratch-built model** has slightly lower train accuracy than val accuracy, suggesting **mild underfitting** but still generalizing well.  
- **Pre-trained models** (VGG16, ResNet50, MobileNetV2, InceptionV3, EfficientNetB0) achieved **extremely high and stable performance**, with no signs of overfitting.


## Accuracy Comparison
<p align="center">
  <img src='Images/model_accuracy_comparison(analysing OF,UF,BM).png'
       width="800"/>
</p>
        
 

## 🚀 Business Impact
- **Positive:**
  - High model accuracy enables reliable fish species identification, useful for fisheries, ecological monitoring, and automated quality control.
  - Multiple high-performing models provide flexibility for deployment (lightweight MobileNetV2 for mobile devices, high-accuracy ResNet50 for server-based systems).
- **Negative:**
  - Larger models (ResNet50, VGG16) require more computational resources, which may increase deployment cost.
  - Dataset-specific tuning might limit model generalization to completely new datasets without retraining.

---

## 🖼️ Visualizations
- Accuracy and loss plots for training and validation phases.
- Confusion matrices for model performance evaluation.
- Precision-Recall curves for in-depth analysis.

---

## 🏆 Conclusion
- **ResNet50** is the recommended choice for deployment due to its **best performance metrics**.
- **MobileNetV2** is the best lightweight alternative for edge or mobile deployments.
- Transfer learning significantly outperforms models trained from scratch on limited data.

---

## 📌 Technologies Used
- **Python**  
- **TensorFlow / Keras**  
- **Matplotlib, Seaborn** (Visualization)  
- **NumPy, Pandas** (Data Handling)
- **scikir-learn (evaluation metrices)

