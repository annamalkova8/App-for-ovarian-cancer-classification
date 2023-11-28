# App-fpr-ovarian-cancer-classification
The app based on ResNet50 CNN to classify the histologic type of ovarian cancer

## Actuality
Ovarian carcinoma is the most lethal cancer of the female reproductive system. There are five common subtypes of ovarian cancer: high-grade serous carcinoma, clear-cell ovarian carcinoma, endometrioid, low-grade serous, and mucinous carcinoma. Recently histological diagnosis has several challenges, including disagreements between observers and the reproducibility of diagnostics. Furthermore, underserved communities often lack access to specialist pathologists, and even well-developed communities face a shortage of pathologists with expertise in gynecologic malignancies.

## The aim of the project
to improve accuracy in identifying ovarian cancer subtypes usin Deep Learning algorithms

## The results
The best results were obtained with ResNet50 module, though the accuracy is quite low.
It might be associated with a small number of samples, high variability of pictures, the lack of possabilty to perform analysis using histolab (to extract details of slices).
The model could classify the test image (HGSC) as CC with 47% of accuracy and as HGSC with 33%.

## Docker container with a model and application
670f665a797145f26a58b0b8b534aa7010fe936aac1278ef60f4fe50bbbf3478

## Link to the model (pickle file)
https://drive.google.com/file/d/1_pWrPE0LOaX55Ljx5doLqH09hsnVJ-Kr/view?usp=sharing
