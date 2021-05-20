from data import train_2
import seaborn as sns
import matplotlib.pyplot as plt


def distrib():
    sns.displot(train_2.SalePrice, kde=True, bins=10)


def heatmap():
    corrmat = train_2.corr()
    f, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(corrmat, square=True, annot=True, cmap="Dark2");


def regplot():
    sns.lmplot(x="OverallQual", y="SalePrice", data=train_2).set(title='Prix de vente et qualite de la propriété')



