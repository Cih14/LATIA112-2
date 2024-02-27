# -*- coding: utf-8 -*-
"""week2_0227.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VI3HIpBKBy4cvvVMc7jzPrEQIt3B0H-o

from google colab import files #匯入套件

import pandas as pd

upload = files.upload() #開啟上傳介面並載入

data = pd.read_csv("剛剛上傳的檔案名稱")
"""

from google.colab import drive
drive.mount('/content/gdrive/', force_remount=True)

import os
os.chdir("/content/gdrive/My Drive/")
!ls -l "/content/gdrive/My Drive/11202_latia/"
#!ls -l "自行填寫正確的路徑"

import pandas as pd

csv_file = './11202_latia/112_student.csv'
#csv_file ="自行填寫正確的路徑"

#columns = [
#    "學年度","學校代碼","學校名稱","日間∕進修別","等級別","總計","男生計",
#    "女生計","一年級男","一年級女","二年級男","二年級女","三年級男","三年級女",
#    "四年級男","四年級女","五年級男","五年級女","六年級男","六年級女",
#    "七年級男","七年級女","延修生男","延修生女","縣市名稱","體系別"
#]
df = pd.read_csv(csv_file, encoding='utf-8')
#print(df.head())

#查看資料欄位資訊
print(df.info())

#查看資料的統計學資訊描述
print(df.describe())

import pandas as pd

csv_file = './112_2_LATIA/week2_022724/titanic_train.csv'

df = pd.read_csv(csv_file, encoding='utf-8')
#print(df.head())

#查看資料欄位資訊
#print(df.info())
print(df.describe(include='all'))

# source = 'https://ithelp.ithome.com.tw/articles/10200686'

#匯入maplotlib做視覺化
import matplotlib.pyplot as plt

#讀取資料
data = pd.read_csv('./112_2_LATIA/week2_022724/titanic_train.csv')

#對Embarked登船港口作計數
data.Embarked.value_counts()

# 對Embarked登船港口作計數畫橫條圖
data.Embarked.value_counts().plot.barh(x='Port of Embarkation', y='number of people')

# 對Embarked登船港口畫圓餅圖
data.Embarked.value_counts().plot(kind='pie')

# 對Pclass購票等級作計數
data.Pclass.value_counts()

# 對Pclass購票等級畫橫條圖
data.Pclass.value_counts().plot.barh(x='Pclasses', y='number of people')

# 對Pclass購票等級畫圓餅圖
data.Pclass.value_counts().plot(kind='pie')

# 對Pclass購票等級畫箱型圖
data.Pclass.value_counts().plot(kind='box')

# 只取Pclass為1的紀錄
class_1 = data.Pclass[data.Pclass == 1]
print('只取Pclass為1的紀錄\n', class_1.head())

# 只取Pclass為2的紀錄
class_2 = data.Pclass[data.Pclass == 2]
print('只取Pclass為2的紀錄\n', class_2.head())

# 只取Pclass為3的紀錄
class_3 = data.Pclass[data.Pclass == 3]
print('只取Pclass為3的紀錄\n', class_3.head())

# 只取Pclass大於1的紀錄
below_1 = data.Pclass[data.Pclass > 1]
print('只取Pclass大於1的紀錄\n', below_1.head())

# 只取Pclass大於2的紀錄
below_2 = data.Pclass[data.Pclass > 2]
print('只取Pclass大於2的紀錄\n', below_2.head())

# 對Fare票價畫長條圖
data.Fare.hist()

# 將資料以Age以及Pclass分群後取Fare之算術平均數的折線圖
data.groupby(['Age', 'Pclass']).mean()['Fare'].plot()

# 顯示所有表徵之間的關聯性
from pandas.plotting import scatter_matrix
scatter_matrix(data, alpha=0.5, diagonal='kde')
plt.show()

# 將票價資料從英鎊轉換為台幣計價
fare_in_twd = data.Fare * 40.8
# 將票價資料從英鎊轉換為美金計價
fare_in_twd = data.Fare * 1.31