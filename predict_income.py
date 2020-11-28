import joblib
from sklearn.linear_model import LinearRegression

def predict_sale_price(jobType,degree,yearsExperience):
    trained_model = joblib.load(r'C:\Users\ASUS\PycharmProjects\grpc\income.pkl')
    prediction = trained_model.predict([[jobType,degree,yearsExperience]])
    return (prediction)