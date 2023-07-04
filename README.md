# MailSVMclassification

pip install -r requirement.txt

# Model update

SVM's kernel is linear pretty useble in another dataset. I tried to train model on "https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv" and to tested model on "https://www.kaggle.com/datasets/venky73/spam-mails-dataset".

## Linear
ConfusionMatrix: [[3619   53][ 501  998]], accuracy score: 89,29%

## Poly
ConfusionMatrix: [[3620   52][ 465 1034]], accuracy score: 90,00%

## Sigmoid
ConfusionMatrix: [[3672    0][1498    1]], accuracy score: 71,03%

## RBF
ConfusionMatrix: [[2279 1393][ 266 1233]], accuracy score: 67,92%