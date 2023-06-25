import os
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, NuSVC
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
import numpy as np
import skops.io as sio

# Bước tiền xử lý: tạo từ điển các từ xuất hiện trong mail train và xóa các từ không có nghia


def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i, line in enumerate(m):
                if i == 2:  # lấy nội dung mail từ dòng thứ 3
                    words = line.split()
                    all_words += words

    dictionary = Counter(all_words)
    # xoa cac tu khong co nghia
    list_to_remove = dictionary.keys()
    for item in list(list_to_remove):
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(5000)
    return dictionary


def extract_features(mail_dir):
    files = [os.path.join(mail_dir, fi) for fi in os.listdir(mail_dir)]
    # Tạo ra một ma trận có kích thước 100x5000 có giá trị =0
    features_matrix = np.zeros((len(files), 5000))
    docID = 0
    for fil in files:
        with open(fil) as fi:
            for i, line in enumerate(fi):
                if i == 2:
                    words = line.split()
                    for word in words:
                        wordID = 0
                        for i, d in enumerate(dictionary):
                            if d[0] == word:
                                wordID = i
                                features_matrix[docID,
                                                wordID] = words.count(word)
            docID = docID + 1
    return features_matrix

def save_dictionary():

    dic = ""
    for element in dictionary:
        dic = dic + element[0] + " "
    with open("dictionary.txt", "w") as f:
        f.write(dic)

# Duong dan den du lieu train
train_dir = 'dataset/mail_train'
# từ điển
dictionary = make_Dictionary(train_dir)
print(dictionary)
save_dictionary()
# np.zeros để tạo mảng 200 phần tử và đánh số 100 phần tử đầu là 0, 100 phần tử sau là 1
train_labels = np.zeros(200)
train_labels[100:200] = 1
print("Train Labels:")
print(train_labels)
# train_matrix mảng 2 chiều có giá trị 0 và 1
train_matrix = extract_features(train_dir)
print("Train Maxtrix:")
print(np.shape(train_matrix))

# Sử dụng thuật toán SVM để học
SVM_model = SVC()
print(SVM_model.fit(train_matrix, train_labels))
# Các tham số điều chỉnh SVM
param_grid = {'C': [10, 100], 'gamma': [0.01, 0.001]}
grid = GridSearchCV(SVC(), param_grid, verbose=3)
#grid.fit(train_matrix, train_labels)

#print('Grid', grid.best_params_)
#print("Grid best estimator", grid.best_estimator_)

# Kiểm tra spam
test_dir = 'dataset/mail_test'
test_matrix = extract_features(test_dir)
test_labels = np.zeros(100)
#test_labels[80:100] = 1
SVM_predictions = SVM_model.predict(test_matrix)
print("SVM predict")
print(SVM_predictions)
print('ket qua')
# Giải thích kết quả,  confusion_matrix:
# Tổng mail test là 100. Thuật toán dự đoán 80 mail là spam  và 20 email không phải spam
# Thực tế có 78 email đúng là mail spam và có 2 email đoán sai
#   Có 19 email không phải spam và có 1 cái đoán sai
print(confusion_matrix(test_labels, SVM_predictions))

obj = sio.dump(SVM_model, "SVM_clf_mail.skops")
# skops.io.load(file, trusted=False)