from data import train_2
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

mod = smf.ols(formula='SalePrice ~ OverallQual + MasVnrArea', data=train_2)
res = mod.fit()


def prediction_mpg(OverallQual, MasVnrArea):
    result = res.params['OverallQual'] * OverallQual + res.params['MasVnrArea'] * MasVnrArea + res.params['Intercept']
    result_min = round((res.rsquared * result), 2)
    result_max = round(((1 - res.rsquared) * result + result), 2)
    return f'cette propriété sera vendu entre {result_min} et {result_max} selon notre model'


def prediction_mpg_one():
    # je multiplie mes coef avec les valeur de mon dataframe pour l'exemple  id
    result = res.params['OverallQual'] * 7 + res.params['MasVnrArea'] * 196 + res.params['Intercept']
    result = round(result, 2)
    print(f" Le prix de la propriete de l'id 0 selon notre model est: {result} au lieu de 208000 dans notre dataframe de base ")


X = train_2[['OverallQual', 'MasVnrArea']]
y = train_2.SalePrice
reg = LinearRegression().fit(X, y)
