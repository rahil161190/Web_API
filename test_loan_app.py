import pytest
from loan_status_predict import app
# make something that mimics the server

@pytest.fixture
def client():
    return app.test_client()

def test_hello_ping(client):
    resp = client.get('/')
    assert resp.data.decode() == 'Hi welcome to Loan Status Prediction'

def test_pinger(client):
    resp = client.get('/ping')
    assert resp.data.decode() == 'Hi I am a pinger'

def test_prediction(client):
    test_data = {
        "Gender": "Male",
        "Married": "Yes",
        "Dependents": "2",
        "Education": "Not Graduate",
        "Self_Employed": "Yes",
        "ApplicantIncome": 10000,
        "CoapplicantIncome": 2000,
        "LoanAmount": 150,
        "Credit_History": "Yes"
    }
    resp = client.post("/predict",json = test_data)
    assert resp.json == {"Loan_approval_status": 1 }