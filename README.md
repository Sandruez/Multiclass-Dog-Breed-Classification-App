# 🐶 Dog Breed Classification

This project focuses on classifying different dog breeds using **deep learning models**.  
Multiple pre-trained architectures were tested and compared against a scratch-built CNN model.

---

## 📂 Dataset
- Images of multiple dog breeds.
- Preprocessed and split into **training** and **validation** sets.
- Balanced, overfitted, and underfitted models were analyzed for performance insights.

---

## 🛠 Models Used
- Scratch CNN (from scratch)
- VGG16
- ResNet50
- MobileNetV2
- InceptionV3
- EfficientNetB0

---

## 📊 Model Results

| Model            | Training Accuracy | Validation Accuracy |
|------------------|------------------:|--------------------:|
| Scratch CNN       | 0.3736            | 0.1115              |
| VGG16             | 0.9198            | 0.6660              |
| ResNet50          | 0.9996            | 0.7550              |
| MobileNetV2       | 0.9640            | 0.7804              |
| InceptionV3       | 0.9911            | 0.8112              |
| EfficientNetB0    | 0.9090            | 0.8210              |

---

## 📈 Performance Chart

![Model Performance](Images/model_performance_analysis(OF,UF,B).png)

---

## 📊 Model Performance & Generalization Analysis

| Model            | Training Accuracy | Validation Accuracy | Generalization Gap | Analysis Type     |
|------------------|------------------|---------------------|--------------------|-------------------|
| Scratch Model    | 0.374             | 0.111               | **-0.263**         | **Underfitting** – model fails to learn patterns from training data. |
| VGG16            | 0.920             | 0.666               | **-0.254**         | **Mild Overfitting** – learns well on training but struggles to generalize. |
| ResNet50         | 0.999             | 0.755               | **-0.244**         | **Overfitting** – memorizes training data, limited generalization. |
| MobileNetV2      | 0.964             | 0.780               | **-0.184**         | **Balanced** – good trade-off between training and validation accuracy. |
| InceptionV3      | 0.991             | 0.811               | **-0.180**         | **Balanced** – strong learning with good generalization. |
| EfficientNetB0   | 0.909             | 0.821               | **-0.088**         | **Well Balanced** – closest match between training and validation performance. |

---

### 🔍 How to Interpret
- **Underfitting** – Low training & validation accuracy. Model is too simple or not trained enough.  
- **Overfitting** – High training accuracy but much lower validation accuracy. Model memorizes rather than generalizes.  
- **Balanced** – High training accuracy and proportionally close validation accuracy, indicating good generalization.

**Insights:**
- The **Scratch model** is clearly **underfitting**.  
- **VGG16** and **ResNet50** show signs of **overfitting**, though not extreme.  
- **MobileNetV2**, **InceptionV3**, and **EfficientNetB0** show **good balance**, with **EfficientNetB0** having the smallest gap.


## 🔍 Observations

- **Underfitting (UF):**  
  The Scratch CNN showed clear underfitting, with both low training and validation accuracy.
  
- **Overfitting (OF):**  
  ResNet50 achieved almost perfect training accuracy but had a noticeable drop in validation accuracy, indicating mild overfitting.
  
- **Balanced Models:**  
  MobileNetV2, InceptionV3, and EfficientNetB0 achieved strong validation accuracy with minimal overfitting.
  
- **Best Performing Model:**  
  EfficientNetB0 had the highest validation accuracy (**82.10%**) despite having slightly lower training accuracy than some models, making it the most generalizable.

---

## 📌 Conclusion
Transfer learning significantly outperformed the scratch-built CNN.  
EfficientNetB0 is recommended for deployment due to its balance between accuracy and generalization.

---

