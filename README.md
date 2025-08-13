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

![Model Performance](https://raw.githubusercontent.com/USERNAME/REPO_NAME/BRANCH_NAME/images/model_performance_clean.png)

---

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

